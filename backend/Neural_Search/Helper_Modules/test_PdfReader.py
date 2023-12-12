import unittest
import PyPDF2
from unittest.mock import MagicMock, mock_open, patch
from PdfReader import pdf_to_text, pdf_to_docVec
from Neural_Search.Helper_Modules.DocVec import DocVec
import numpy as np


class TestPdfProcessing(unittest.TestCase):

    @patch('PyPDF2.PdfReader')
    def test_pdf_to_text(self, mock_pdf_reader):
        # Mocking the PyPDF2 PdfReader and its pages
        mock_pdf_reader.return_value.pages = [MagicMock(extract_text=lambda: "First page. \n"),
                                              MagicMock(extract_text=lambda: "Second page.")]

        with patch('builtins.open', mock_open(read_data="dummy data")):
            result = pdf_to_text("dummy_path.pdf")

        self.assertIn("First page", result['text'])
        self.assertIn("Second page", result['text'])
        self.assertEqual(len(result['paragraphs']), 2)  # Assuming each page ends with a period followed by a newline

    @patch('PyPDF2.PdfReader')
    def test_pdf_to_docVec(self, mock_pdf_reader):
        # Mocking the PyPDF2 PdfReader
        mock_pdf_reader.return_value.pages = [MagicMock(extract_text=lambda: "Test paragraph.")]

        # Mocking the encoder
        mock_encoder = MagicMock()
        mock_encoder.encode = MagicMock(side_effect=[np.array(["doc_vec"]), np.array(["para_vec"])])

        with patch('builtins.open', mock_open(read_data="dummy data")):
            docVec = pdf_to_docVec("dummy_path.pdf", mock_encoder)

        self.assertIsInstance(docVec, DocVec)
        self.assertEqual(docVec.vec, ["doc_vec"])
        self.assertEqual(len(docVec.paras_vecs), 1)
        self.assertEqual(docVec.paras_vecs[0]["vec"], ["para_vec"])

    def pdf_to_text(path):
        pdffileobj = open(path, 'rb')
        pdfreader = PyPDF2.PdfReader(pdffileobj)
        extracted_text = ""

        for page in pdfreader.pages:
            page_text = page.extract_text()
            if page_text is not None:
                extracted_text += page_text
        paragraphs = extracted_text.split(". \n")

        return {'text': extracted_text, 'paragraphs': paragraphs}

    @patch('PyPDF2.PdfReader')
    def test_pdf_to_docVec_varied_paragraphs(self, mock_pdf_reader):
        # Mocking PDF reader with specified text
        mock_pdf_reader.return_value.pages = [
            MagicMock(extract_text=lambda: "Paragraph 1. \nParagraph 2. \n"),
            MagicMock(extract_text=lambda: "Paragraph 3. \n")
        ]

        # Adjusted mock_encode function
        def mock_encode(text):
            if text.strip() == "Paragraph 1. Paragraph 2. Paragraph 3":  # The full document text
                return np.array(["doc_vec"])
            else:
                # Adjust the paragraph text format
                return np.array([text.strip().replace(". \n", ".") + "_vec"])

        mock_encoder = MagicMock()
        mock_encoder.encode.side_effect = mock_encode

        with patch('builtins.open', mock_open(read_data="dummy data")):
            docVec = pdf_to_docVec("dummy_path.pdf", mock_encoder)

        self.assertEqual(len(docVec.paras_vecs), 3)
        self.assertEqual(docVec.paras_vecs[0]["vec"], ["Paragraph 1_vec"])
        self.assertEqual(docVec.paras_vecs[1]["vec"], ["Paragraph 2_vec"])
        self.assertEqual(docVec.paras_vecs[2]["vec"], ["Paragraph 3_vec"])

    @patch('PyPDF2.PdfReader')
    def test_pdf_to_text_large_pdf(self, mock_pdf_reader):
        mock_pdf_reader.return_value.pages = [MagicMock(extract_text=lambda: f"Page {i}. \n") for i in range(1, 101)]

        with patch('builtins.open', mock_open(read_data="dummy data")):
            result = pdf_to_text("large_dummy_path.pdf")

        # Check if the text from the first and last pages is present
        self.assertIn("Page 1", result['text'])
        self.assertIn("Page 100", result['text'])
        # Check the paragraph count
        self.assertEqual(len(result['paragraphs']), 100)

    @patch('builtins.open', new_callable=mock_open, read_data="dummy data")
    @patch('PyPDF2.PdfReader')

    def test_pdf_to_text_exception_handling(self, mock_pdf_reader, mock_file):
        # Setting the side effect of PyPDF2.PdfReader to raise an exception
        mock_pdf_reader.side_effect = Exception("Error reading PDF")

        # Test to ensure that an exception is raised
        with self.assertRaises(Exception) as context:
            result = pdf_to_text("faulty_path.pdf")

        # Optionally, assert the message of the exception if needed
        self.assertEqual(str(context.exception), "Error reading PDF")

    def test_pdf_to_docVec_exception_handling(self):
        with patch('builtins.open', mock_open(read_data="dummy data")):
            with patch('PyPDF2.PdfReader', side_effect=Exception("Error reading PDF")):
                with self.assertRaises(Exception):
                    pdf_to_docVec("faulty_path.pdf", MagicMock())


if __name__ == '__main__':
    unittest.main()
