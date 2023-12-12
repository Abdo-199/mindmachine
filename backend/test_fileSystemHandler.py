import unittest
from unittest.mock import patch, MagicMock
from fileSystemHandler import FileSystemHandler

class MockFile:
    def __init__(self, name):
        self.filename = name
        self.file = MagicMock()
        self.file.read = MagicMock(return_value="file content")

class TestFileSystemHandler(unittest.TestCase):

    def setUp(self):
        self.mock_qd_client = MagicMock()
        self.file_system_handler = FileSystemHandler(self.mock_qd_client)

    def test_init(self):
        self.assertEqual(self.file_system_handler.qdClient, self.mock_qd_client)

    # def test_upload_success(self):
    #     user_id = 'test_user'
    #     files = [MockFile('file1.pdf'), MockFile('file2.pdf')]
    #
    #     with patch('builtins.open', unittest.mock.mock_open()) as mock_file, \
    #             patch('os.path.join', return_value=r'/Users/mouhebkhairallah/Desktop/mindmachine/backend') as mock_join, \
    #             patch('fileSystemHandler.pdf_to_docVec') as mock_pdf_to_docVec:
    #         self.file_system_handler.upload(user_id, files)
    #         mock_file.assert_called()
    #         mock_join.assert_called()
    #         mock_pdf_to_docVec.assert_called()
    #         # Add more assertions based on what upload method does

    def test_upload_success(self):
        user_id = 'test_user'
        files = [MockFile('file1.pdf'), MockFile('file2.pdf')]

        with patch('fileSystemHandler.FileSystemHandler.file_system_exist', return_value=None) as mock_file_system_exist, \
             patch('builtins.open', unittest.mock.mock_open()) as mock_file, \
             patch('os.path.join', return_value='/path/to/mindmachine/backend/file1.pdf') as mock_join, \
             patch('fileSystemHandler.pdf_to_docVec') as mock_pdf_to_docVec:
            self.file_system_handler.upload(user_id, files)
            mock_file_system_exist.assert_called_with(user_id=user_id)
            mock_file.assert_called()
            mock_join.assert_called()
            mock_pdf_to_docVec.assert_called()
            # Add more assertions based on what upload method does

    # def test_delete_document(self):
    #     expected_file_path = ...
    #     with patch('os.remove') as mock_remove:
    #         os.remove(expected_file_path)  # Directly call for debugging
    #         mock_remove.assert_called_with(expected_file_path)

    def test_delete_document(self):
        user_id = 'test_user'
        document_id = 'file2.pdf'
        expected_file_path = f"/usr/src/app/mm_docs/user/{user_id}/{document_id}"

        with patch('os.path.exists', return_value=True) as mock_exists, \
                patch('os.remove') as mock_remove:
            self.file_system_handler.delete_document(user_id, document_id)
            mock_exists.assert_called_with(expected_file_path)
            mock_remove.assert_called_with(expected_file_path)

    # def test_get_fs_for_user(self):
    #     user_id = 'test_user'
    #     expected_files = [{'file_name': 'file1.pdf', 'file_size': '1.00 MB', 'file_date': '2021-01-01'}]
    #     with patch('os.listdir', return_value=['file1.pdf']), \
    #          patch('os.path.getsize', return_value=1024 * 1024), \
    #          patch('fileSystemHandler.FileSystemHandler.get_last_modified_date', return_value='2021-01-01'):
    #         result = self.file_system_handler.get_fs_for_user(user_id)
    #         self.assertEqual(result, expected_files)

    # def test_get_fs_for_user(self):
    #     user_id = 'test_user'
    #     expected_files = [{'file_name': 'file1.pdf', 'file_size': '1.00 MB', 'file_date': '2021-01-01'}]
    #
    #     with patch('os.listdir', return_value=['file1.pdf']) as mock_listdir, \
    #             patch('os.path.getsize', return_value=1024 * 1024) as mock_getsize, \
    #             patch('fileSystemHandler.FileSystemHandler.get_last_modified_date',
    #                   return_value='2021-01-01') as mock_get_last_modified_date:
    #         # Call the method and capture the result
    #         result = self.file_system_handler.get_fs_for_user(user_id)
    #
    #         # Print statements for debugging
    #         print("Mocked os.listdir return value:", mock_listdir.return_value)
    #         print("Mocked os.path.getsize return value:", mock_getsize.return_value)
    #         print("Mocked get_last_modified_date return value:", mock_get_last_modified_date.return_value)
    #         print("Result from get_fs_for_user:", result)
    #
    #         # Assertion to check if the result matches the expectation
    #         self.assertEqual(result, expected_files)

    # def test_get_fs_for_user(self):
    #     user_id = 'test_user'
    #     expected_files = [{'file_name': 'file1.pdf', 'file_size': '1.00 MB', 'file_date': '2021-01-01'}]
    #
    #     # Mock root_directory to a safe path for testing
    #     test_root_directory = r'/Users/mouhebkhairallah/Desktop/mindmachine/backend'
    #
    #     with patch('fileSystemHandler.config.root_directory', test_root_directory), \
    #             patch('os.listdir', return_value=['file1.pdf']), \
    #             patch('os.path.getsize', return_value=1024 * 1024), \
    #             patch('fileSystemHandler.FileSystemHandler.get_last_modified_date', return_value='2021-01-01'):
    #         result = self.file_system_handler.get_fs_for_user(user_id)
    #         self.assertEqual(result, expected_files)

    def test_get_fs_for_user(self):
        user_id = 'test_user'
        expected_files = [{'file_name': 'file1.pdf', 'file_size': '1.00 MB', 'file_date': '2021-01-01'}]

        with patch('fileSystemHandler.FileSystemHandler.file_system_exist',
                   return_value=None) as mock_file_system_exist, \
                patch('os.listdir', return_value=['file1.pdf']) as mock_listdir, \
                patch('os.path.getsize', return_value=1024 * 1024) as mock_getsize, \
                patch('fileSystemHandler.FileSystemHandler.get_last_modified_date',
                      return_value='2021-01-01') as mock_get_last_modified_date:
            result = self.file_system_handler.get_fs_for_user(user_id)

            mock_file_system_exist.assert_called_with(user_id=user_id)
            mock_listdir.assert_called_with('/usr/src/app/mm_docs/user/' + user_id)
            mock_getsize.assert_called()
            mock_get_last_modified_date.assert_called()

            self.assertEqual(result, expected_files)

    def test_edit_document_name(self):
        user_id = 'test_user'
        old_name = 'old_file.pdf'
        new_name = 'new_file.pdf'
        with patch('os.path.exists', return_value=True), \
             patch('os.rename') as mock_rename:
            self.file_system_handler.edit_document_name(user_id, old_name, new_name)
            mock_rename.assert_called_with('/usr/src/app/mm_docs/user/test_user/old_file.pdf', '/usr/src/app/mm_docs/user/test_user/new_file.pdf')

    def test_get_document_path(self):
        user_id = 'test_user'
        document_name = 'file.pdf'
        expected_file_path = f"/usr/src/app/mm_docs/user/{user_id}/{document_name}"
        with patch('os.path.exists', return_value=True):
            result = self.file_system_handler.get_document_path(user_id, document_name)
            self.assertEqual(result, expected_file_path)


    def test_file_system_exist(self):
        user_id = 'test_user'
        with patch('os.path.exists', return_value=False), \
             patch('os.makedirs') as mock_makedirs:
            self.file_system_handler.file_system_exist(user_id)
            mock_makedirs.assert_called_with('/usr/src/app/mm_docs/user/test_user')

    def test_convert_bytes(self):
        byte_sizes = [500, 1024, 1048576]  # 500B, 1KB, 1MB
        expected_results = ['500.00 B', '1.00 KB', '1.00 MB']
        for size, expected in zip(byte_sizes, expected_results):
            result = self.file_system_handler.convert_bytes(size)
            self.assertEqual(result, expected)

    def test_get_last_modified_date(self):
        file_path = 'path/to/file'
        expected_date = '01.01.2021'
        with patch('os.stat', return_value=MagicMock(st_mtime=1609459200)):  # Timestamp for 2021-01-01
            result = self.file_system_handler.get_last_modified_date(file_path)
            self.assertEqual(result, expected_date)

if __name__ == '__main__':
    unittest.main()