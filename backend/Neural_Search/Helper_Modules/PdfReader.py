import PyPDF2
from Neural_Search.Helper_Modules.DocVec import DocVec


''''
Issues with the original Function

1. Inefficient Paragraph Splitting: The line paragraphs = extracted_text.split(". \n") 
   was inside the loop iterating over the pages. This meant that the entire text was 
   being split into paragraphs on every iteration, which was inefficient and could lead 
   to incorrect splitting if a paragraph spanned multiple pages.

2. Extra Empty Paragraph: The splitting logic could potentially add an extra empty 
   paragraph if the text ended with the delimiter ". \n".



Changes Made and Reasons

1. Paragraph Splitting Moved Outside the Loop: The line for splitting text into paragraphs 
    was moved outside of the page iteration loop. This change ensures that the splitting 
    happens only once after all pages have been concatenated. 

Why changed:

1.  It improves efficiency and correctly handles paragraphs that span multiple pages.

2.  Filtering Out Empty Paragraphs: Added a line to filter out any empty or whitespace-only
      paragraphs. This change addresses the issue where the text ending with the delimiter ". \n" 
      resulted in an additional, undesired empty paragraph.

1. Efficiency: Reduces unnecessary computations within the loop, making the function more efficient.

2. Accuracy: Improves the accuracy of paragraph splitting, ensuring that paragraphs spanning multiple pages are 
    handled correctly and no extra empty paragraphs are included.


'''

def pdf_to_text(path):
  pdffileobj = open(path, 'rb')
  pdfreader = PyPDF2.PdfReader(pdffileobj)
  extracted_text = ""

  for page in pdfreader.pages:
    extracted_text += page.extract_text()

  paragraphs = extracted_text.split(". \n")

  # Remove any empty paragraphs
  paragraphs = [p for p in paragraphs if p.strip()]

  return {'text': extracted_text, 'paragraphs': paragraphs}


def pdf_to_docVec(path, encoder):
  doc = pdf_to_text(path)
  vec = encoder.encode(doc['text']).tolist()

  paras_vecs = []
  for idp, para in enumerate(doc['paragraphs']):
    paras_vecs.append({"paragraph":para,"vec":encoder.encode(para).tolist()})

  return DocVec(path, vec, paras_vecs)