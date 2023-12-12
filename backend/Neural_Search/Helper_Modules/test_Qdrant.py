import unittest
from unittest.mock import MagicMock
from Qdrant import Qdrant
import numpy as np


class TestQdrant(unittest.TestCase):

    def setUp(self):
        self.qdrant = Qdrant()
        self.qdrant.qdrant_client = MagicMock()

    def test_check_user_existing(self):
        # Simulate existing user
        self.qdrant.qdrant_client.get_collection.return_value = MagicMock(vectors_count=10)

        vectors_count = self.qdrant.check_user("existing_user")
        self.assertEqual(vectors_count, 10)
        self.qdrant.qdrant_client.get_collection.assert_called_once_with("existing_user")

    def test_check_user_non_existing(self):
        # Simulate non-existing user
        self.qdrant.qdrant_client.get_collection.side_effect = Exception("User does not exist")
        self.qdrant.qdrant_client.create_collection = MagicMock()

        vectors_count = self.qdrant.check_user("new_user")
        self.assertEqual(vectors_count, 0)
        self.qdrant.qdrant_client.create_collection.assert_called_once()

    def test_add_docVec(self):
        self.qdrant.check_user = MagicMock(return_value=0)
        self.qdrant.qdrant_client.upload_records = MagicMock()

        docVec = MagicMock()
        docVec.vec = [1, 2, 3]
        docVec.name = "Document1"
        docVec.paras_vecs = [{'vec': [1, 2], 'paragraph': "Para1"}, {'vec': [3, 4], 'paragraph': "Para2"}]

        self.qdrant.add_docVec("user1", docVec)

        self.qdrant.check_user.assert_called_once_with("user1")
        self.assertEqual(self.qdrant.qdrant_client.upload_records.call_count, 3)  # One for the doc and two for paragraphs

    def test_get_hits(self):
        # Mock the encoder to return a numpy array
        self.qdrant.encoder.encode = MagicMock(return_value=np.array([1, 2, 3]))

        # Mock the search function of the Qdrant client
        self.qdrant.qdrant_client.search = MagicMock()

        # Define the filter (assuming it's correctly instantiated)
        filter = MagicMock()

        # Call the get_hits method
        self.qdrant.get_hits("collection1", "search text", filter)

        # Assert that the search method was called correctly
        self.qdrant.qdrant_client.search.assert_called_once()

    def test_get_scores(self):
        hits = [MagicMock(score=0.9, payload={"name": "Doc1"}), MagicMock(score=0.7, payload={"name": "Doc2"})]

        result = self.qdrant.get_scores(hits)

        self.assertEqual(result, "Doc1")

    def test_search(self):
        self.qdrant.get_hits = MagicMock()
        self.qdrant.get_scores = MagicMock(side_effect=["Doc1", "Para1"])

        result = self.qdrant.search("collection1", "search text")

        self.assertEqual(result, {"relevant_doc": "Doc1", "relevant_paragraph": "Para1"})
        self.assertEqual(self.qdrant.get_hits.call_count, 2)
        self.assertEqual(self.qdrant.get_scores.call_count, 2)


# More tests for other methods...

if __name__ == '__main__':
    unittest.main()
