"""
DocVec Class

Author: Abdelrahman Elsharkawi
Creation Date: 11.11.2023
"""
import os

class DocVec:
  """
  Class representing a document vector.

  Attributes:
  - path (str): Path to the document.
  - name (str): Name of the document (extracted from the path).
  - vec: Document vector.
  - paras_vecs: List of dictionaries containing paragraph vectors and corresponding text
  [{"paragraph":"","vec":""}].
  """
  def __init__(self, path, vec, paras_vecs):
    """
    Initialize the DocVec class.

    Parameters:
    - path (str): Path to the document.
    - vec: Document vector.
    - paras_vecs: List of dictionaries containing paragraph vectors and corresponding text
    [{"paragraph":"","vec":""}].
    Returns:
    None
    """
    self.path = path
    self.name = os.path.basename(path)
    self.vec = vec
    self.paras_vecs = paras_vecs