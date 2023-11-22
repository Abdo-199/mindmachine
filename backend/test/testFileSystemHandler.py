import unittest
import os
from datetime import datetime
from unittest.mock import Mock

from backend.fileSystemHandler import FileSystemHandler


class TestFileSystemHandlerMethods(unittest.TestCase):
    def setUp(self):

        self.handler_instance = FileSystemHandler()

    def tearDown(self):

        user_id = "test_user"
        document_id = "test_document.txt"
        user_directory = os.path.join(self.handler_instance.root_directory, user_id)
        document_path = os.path.join(user_directory, document_id)

        if os.path.exists(document_path):
            os.remove(document_path)
        if os.path.exists(user_directory):
            os.rmdir(user_directory)

    def test_upload(self):
        user_id = "test_user"
        mock_file = Mock()
        mock_file.filename = "test_file.txt"
        mock_file.file.read.return_value = b'Test file content'

        self.handler_instance.upload(user_id, [mock_file])

        file_path = os.path.join(self.handler_instance.root_directory + user_id, mock_file.filename)
        self.assertTrue(os.path.exists(file_path), "File was not created.")
        with open(file_path, "rb") as f:
            content = f.read()
        self.assertEqual(content, b'Test file content', "File content does not match.")



if __name__ == '__main__':
    unittest.main()
