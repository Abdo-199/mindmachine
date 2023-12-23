'''
A script with methods to read the dataset, encode PDF documents, compare search results with true results, and visualize accuracy per category.

A script is better than a class in this case to enabl the static usage of the single methods easier.

'''

import os
import re
import matplotlib.pyplot as plt
import seaborn as sns
from Qdrant import Qdrant
from PdfReader import pdf_to_docVec


def find_pdf_files(directory):
    """
    Finds all PDF files in a given directory and its subdirectories.

    Parameters:
        directory (str): The root directory to search for PDF files.

    Returns:
        list: A list of paths to PDF files.
    """
    pdf_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                pdf_files.append(os.path.join(root, file))
    return pdf_files


def encode_dataset(name, encoder, path):
    """
    Encodes PDF documents in a given directory using a specified encoder and adds them to the Qdrant index.

    Parameters:
        name (str): The name of the dataset.
        encoder: The encoder used to convert PDFs to document vectors.
        path (str): The path to the directory containing PDF files.
    """
    qdClient = Qdrant(encoder)
    pdf_paths = find_pdf_files(path)
    for pdf in pdf_paths:
        qdClient.add_docVec(name, pdf_to_docVec(pdf, encoder))
        print(pdf)


def parse_text_file(file_path):
    """
    Parses the content of a text file containing information about PDFs and their Q&A pairs.

    Parameters:
        file_path (str): The path to the text file.

    Returns:
        dict: A dictionary containing parsed data with PDF titles and corresponding Q&A pairs.
    """
    with open(file_path, 'r') as file:
        content = file.read()

    # Splitting the content into sections for each PDF
    sections = content.split("###")[1:]  # Skip the first split as it will be empty
    parsed_data = {}

    for section in sections:
        # Extracting PDF title
        title_match = re.search(r'PDF \d+: (.+)', section)
        if title_match:
            title = title_match.group(1)
            parsed_data[title] = []

            # Finding all Q&A pairs
            qa_pairs = re.findall(r'\*\*Question:\*\* (.*?)\n   \*\*Answer:\*\* "(.*?)"', section)
            for question, answer in qa_pairs:
                parsed_data[title].append({'Question': question, 'Answer': answer})

    return parsed_data


def read_dataset(dataset_path):
    """
    Reads a dataset from a specified path containing multiple languages, categories, and text files.

    Parameters:
        dataset_path (str): The path to the root directory of the dataset.

    Returns:
        dict: A nested dictionary representing the dataset structure.
        {'Language': {'category': {'file name': [{'Question': '','Answer': ''},],}}}
    """
    dataset = {}

    for language in os.listdir(dataset_path):
        language_path = os.path.join(dataset_path, language)
        if os.path.isdir(language_path):
            dataset[language] = {}

            for category in os.listdir(language_path):
                category_path = os.path.join(language_path, category)
                if os.path.isdir(category_path):
                    dataset[language][category] = {}

                    for file in os.listdir(category_path):
                        if file.endswith('.txt'):
                            file_path = os.path.join(category_path, file)
                            dataset[language][category] = parse_text_file(file_path)

    return dataset


def is_correct_answer(model_answer, actual_answer):
    """
    Calculates the partial match percentage between two strings using Jaccard similarity.

    Parameters:
        model_answer (str): The answer generated by the language model.
        actual_answer (str): The ground truth answer.

    Returns:
        tuple: A tuple containing the similarity score and a boolean indicating whether the match is above a threshold.
    """
    set1 = set(actual_answer.lower().split())
    set2 = set(model_answer.lower().split())

    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))

    similarity_score = intersection / union

    threshold = 0.4

    return similarity_score, similarity_score >= threshold


def get_model_answer(question, name, client):
    """
    Retrieves the model's answer for a given question using the Qdrant client.

    Parameters:
        question (str): The input question.
        name (str): The name of the dataset.
        client: The Qdrant client for searching.

    Returns:
        dict: A dictionary containing the model's answer including relevant paragraphs and documents.
    """
    return client.search(name, question)


def test_language_model(test_name, dataset_path):
    """
    Tests the language model on a dataset and calculates accuracy per language and category.

    Parameters:
        test_name (str): The name of the test.
        dataset_path (str): The path to the dataset.

    Returns:
        dict: A dictionary containing accuracy results per language and category.
    """
    qdClient = Qdrant()
    dataset = read_dataset(dataset_path)
    results = {}

    for language in dataset:
        results[language] = {}
        for category in dataset[language]:
            correct_count_para = 0
            correct_count_doc = 0
            total_questions = 0

            for pdf in dataset[language][category]:
                for qa in dataset[language][category][pdf]:
                    model_answer = get_model_answer(qa['Question'], test_name, qdClient)

                    similarity_score_para, is_partial_match_para = is_correct_answer(
                        model_answer['relevant_paragraphs'][0], qa['Answer'])

                    if is_partial_match_para:
                        correct_count_para += 1
                    if (model_answer['relevant_docs'][0].split('.')[0] == pdf):
                        correct_count_doc += 1
                    total_questions += 1

            if total_questions > 0:
                accuracy_para = correct_count_para / total_questions
                accuracy_doc = correct_count_doc / total_questions
                results[language][category] = {
                    'accuracy_para': accuracy_para,
                    'accuracy_doc': accuracy_doc,
                    'total_questions': total_questions,
                    'correct_answers_para': correct_count_para
                }
            else:
                results[language][category] = {
                    'accuracy_para': None,
                    'accuracy_doc': None,
                    'total_questions': 0,
                    'correct_answers_para': 0
                }

    return results


def display_acc_per_lang(test_results, language, accuracy):
    """
    Displays a bar plot of accuracy per category for a given language.

    Parameters:
        test_results (dict): The accuracy results from testing the language model.
        language (str): The language for which to display accuracy.
        accuracy (str): The type of accuracy to display (e.g., 'accuracy_para' or 'accuracy_doc').
    """
    # Plotting accuracy per category for a given language
    categories = list(test_results[language].keys())
    accuracies = [test_results[language][category][accuracy] for category in categories]

    plt.figure(figsize=(10, 6))
    sns.barplot(x=categories, y=accuracies)
    plt.title(f'Accuracy per Category in {language}')
    plt.ylabel('Accuracy')
    plt.xlabel('Category')
    plt.xticks(rotation=45)
    plt.show()

# Example usage
# dataset_path = '..\\Dataset\\PDFS'  
# dataset = read_dataset(dataset_path)
# test_results = test_language_model(dataset)
# display_acc_per_lang(test_results, "German")
