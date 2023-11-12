from qdrant_client import QdrantClient

class QDrant:

    def __init__(self) -> None:
        self.client = QdrantClient()

        pass

    def create_collection(self, collection_name):
        self.client.create_collection(collection_name)
        pass

    def add_vectors(self, collection_name, vectors):
        self.client.insert(collection_name, vectors)
        pass

    def delete_vectors(self, collection_name, vector_ids):
        self.client.delete(collection_name, vector_ids)
        pass

    def search(self):
        pass

    # get used disk space
    def get_disk_usage(self):
        pass
