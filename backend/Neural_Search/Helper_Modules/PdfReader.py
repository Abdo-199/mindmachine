import PyPDF2
from sentence_transformers import SentenceTransformer
from Helper_Modules.DocVec import DocVec


def pdf_to_text(path):
  pdffileobj=open(path,'rb')
  pdfreader=PyPDF2.PdfReader(pdffileobj)
  extracted_text = ""

  for page in pdfreader.pages:
    extracted_text += page.extract_text()
    paragraphs = extracted_text.split(". \n")

  return {'text':extracted_text, 'paragraphs':paragraphs}

def pdf_to_docVec(path, encoder):
  doc = pdf_to_text(path)
  vec = encoder.encode(doc['text']).tolist()

  paras_vecs = []
  for idp, para in enumerate(doc['paragraphs']):
    paras_vecs.append({"paragraph":para,"vec":encoder.encode(para).tolist()})

  return DocVec(path, vec, paras_vecs)