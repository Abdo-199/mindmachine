"""
PDF Helper Functions

Author: Abdelrahman Elsharkawi
Creation Date: 11.11.2023
"""
import PyPDF2
from Neural_Search.DocVec import DocVec
import re
import logHandler
from docx import Document

logger = logHandler.LogHandler(name="PdfReader").get_logger()


def exclude_special_characters(input_string):
    """
    Exclude all chars except numbers and letters from the input string.

    Parameters:
    - input_string (str): Input string.

    Returns:
    str: String with special characters removed.
    """
    result = re.sub(r'[^\w\s]', '', input_string.replace('\n', ''))
    return result


def pdf_to_text(path):
    """
  Convert PDF file to plain text.

  Parameters:
  - path (str): Path to the PDF file.

  Returns:
  dict: {'text':extracted_text, 'paragraphs':paragraphs}.
  """
    logger.debug(f"Converting {path} to text")
    pdffileobj = open(path, 'rb')
    pdfreader = PyPDF2.PdfReader(pdffileobj)
    extracted_text = ""

    for i, page in enumerate(pdfreader.pages):
        logger.debug(f"Extracting text from page {i}")
        extracted_text += page.extract_text()
        paragraphs = [exclude_special_characters(p) for p in extracted_text.split(". \n")]

    return {'text': extracted_text, 'paragraphs': paragraphs}


def docx_to_text(path):
    doc = Document(path)
    full_text = []

    for para in doc.paragraphs:
        text = para.text.strip()  # Remove leading/trailing whitespace
        if text:  # Check if the paragraph is not empty after stripping
            full_text.append(text)

    # Combine into a single string
    combined_text = '\n'.join(full_text)
    return {'text': combined_text, 'paragraphs': full_text}


''''
Edited the pdf_to_docVec function to accept the docx files alongwith pdf
and hence changed the name of the function to more generic form from pdf_to_docVec
to file_to_docVec.

However, the orginial function is still there and commented out for time being
so that if the new changes do some harm, you can uncomment the original function

'''


def pdf_to_docVec(path, encoder): #suggestion to change the name from pdf to more general like file_to_docVec
    """
Convert PDF file to DocVec object.

Parameters:
- path (str): Path to the PDF file.
- encoder: Sentence embeddings encoder.

Returns:
DocVec: DocVec object containing document vectors and paragraph vectors.
"""
    logger.debug(f"Converting {path} to DocVec")

    if path.endswith('.pdf'):
        doc = pdf_to_text(path)
    elif path.endswith('.docx'):
        doc = docx_to_text(path)
    else:
        raise ValueError("Unsupported file format")

    vec = encoder.encode(doc['text']).tolist()

    paras_vecs = []
    for idp, para in enumerate(doc['paragraphs']):
        paras_vecs.append({"paragraph": para, "vec": encoder.encode(para).tolist()})

    return DocVec(path, vec, paras_vecs)

# def pdf_to_docVec(path, encoder):
#     """
#   Convert PDF file to DocVec object.
#
#   Parameters:
#   - path (str): Path to the PDF file.
#   - encoder: Sentence embeddings encoder.
#
#   Returns:
#   DocVec: DocVec object containing document vectors and paragraph vectors.
#   """
#     logger.debug(f"Converting {path} to DocVec")
#     doc = pdf_to_text(path)
#     vec = encoder.encode(doc['text']).tolist()
#
#     paras_vecs = []
#     for idp, para in enumerate(doc['paragraphs']):
#         paras_vecs.append({"paragraph": para, "vec": encoder.encode(para).tolist()})
#
#     return DocVec(path, vec, paras_vecs)
