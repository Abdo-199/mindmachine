class DocVec:
  """
  paras_vecs: [{"paragraph":"content", "vec":"equivalent vector"}]
  """
  def __init__(self, path, vec, paras_vecs):
    self.path = path
    self.name = path.split("/")[-1]
    self.vec = vec
    self.paras_vecs = paras_vecs