from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

class QDrant:

    def __init__(self, host='localhost', port=6333) -> None:
        self.client = QdrantClient(host=host, port=port)
#        self.client = QdrantClient()
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        pass

    def text_to_vector(self, text):
        return self.model.encode([text])[0]

    def add_text_as_vector(self, collection_name, text, vector_id):
        vector = self.text_to_vector(text)
        self.client.add(
            collection_name,
            payloads=[{'vector_id': vector_id, 'vector': vector}]
        )


    def create_collection(self, collection_name):
        self.client.create_collection(collection_name)
        pass

    def add_vectors(self, collection_name, vectors):
        self.client.add(collection_name, vectors)
        pass

    def delete_vectors(self, collection_name, vector_ids):
        self.client.delete(collection_name, vector_ids)
        pass

    def search_vectors(self, collection_name, query_vector, top_k=10):
        return self.client.search(collection_name, query_vector, top_k)

    # get used disk space
    def get_disk_usage(self):
        pass
