from qdrant_client import QdrantClient, models
from qdrant_client.http.models import Filter, FieldCondition, MatchValue

class Qdrant:

  def __init__(self, url, api_key, encoder):
    self.encoder = encoder
    self.qdrant_client = QdrantClient(
      url=url,
      api_key=api_key,
    )

  def check_user(self, userName):
    try:
      vectors_count = self.qdrant_client.get_collection(userName).vectors_count
      print(f"user: {userName} exists, and has {vectors_count} vectors")
    except:
      print(f"user doesn't exist, creating a new collection with the user name: {userName}")
      self.qdrant_client.create_collection(
        collection_name=userName,
        vectors_config=models.VectorParams(
            size=self.encoder.get_sentence_embedding_dimension(),
            distance=models.Distance.COSINE,
        ),
      )
      vectors_count = 0
    return vectors_count

  def add_docVec(self, userName, docVec):

    vectors_count = self.check_user(userName)
    self.qdrant_client.upload_records(
    collection_name=userName,
    records=[
        models.Record(id=vectors_count, vector=docVec.vec, payload={"isDoc":True, "name":docVec.name})
    ])
    vectors_count = vectors_count + 1

    for para in docVec.paras_vecs:
      print(para['paragraph'])
      self.qdrant_client.upload_records(
      collection_name=userName,
      records=[
          models.Record(id=vectors_count, vector=para['vec'], payload={"isDoc":False,"name":para['paragraph'], "source_doc":docVec.name})
      ])
      vectors_count = vectors_count + 1


  def get_hits(self, collection_name, search_text, filter):
    return self.qdrant_client.search(
      collection_name= collection_name,
      query_vector= self.encoder.encode(search_text).tolist(),
      query_filter= filter,
      limit=8,
    )

  def get_scores(self, search_text, hits):
    max_score_value = -1
    max_score_value_indoc = None
    for hit in hits:
        print(hit.payload, "score:", hit.score)
        if hit.score > max_score_value:
            max_score_value = hit.score
            max_score_value_indoc = hit.payload

    if max_score_value_indoc is not None:
        print("The Vector with the highst score:", max_score_value_indoc["name"])
        return max_score_value_indoc["name"]
    else:
        print("No vector")
        return "none"

  def search(self, collection_name, search_text):
    docs_filter = Filter(must=[FieldCondition(key="isDoc", match=MatchValue(value=True))])
    docs_hits = self.get_hits(collection_name, search_text, docs_filter)
    relevant_doc = self.get_scores(search_text, docs_hits)

    paras_filter = Filter(must=[FieldCondition(key="source_doc", match=MatchValue(value=relevant_doc))])
    paras_hits = self.get_hits(collection_name, search_text, paras_filter)
    relevant_doc = self.get_scores(search_text, paras_hits)