import os
import config
from datetime import datetime
from Neural_Search.Helper_Modules.PdfReader import pdf_to_docVec

class FileSystemHandler:
    
    def __init__(self, qdClient):
        self.root_directory = config.root_directory
        self.file_extension = config.file_extension
        self.qdClient = qdClient

    # the Document will be uploaded to the file system and at the same time will be encoded and saved in qdrant
    def upload(self, user_id, files):
        self.file_system_exist(user_id=user_id)

        for file in files:
            file_path = os.path.join(self.root_directory + user_id, file.filename)
            with open(file_path, "wb") as f:
                f.write(file.file.read())
                docVec = pdf_to_docVec(file_path, self.qdClient.encoder)
                self.qdClient.add_docVec(user_id, docVec)

    def get_fs_for_user(self, user_id):

        file_name_size = []
        self.file_system_exist(user_id=user_id)

        # Only search for files with a certain extension, see file_extension in config.py
        files = [file for file in os.listdir(self.root_directory + user_id) if file.endswith(self.file_extension)]

        for file_name in files:

            file_path = os.path.join(self.root_directory + user_id, file_name)
            file_size = os.path.getsize(file_path)

            # Convert Bytes to Megabytes
            file_size = self.convert_bytes(file_size)

            file_upload_date = self.get_last_modified_date(file_path)

            # Frontend Format
            file_name_size.append({'file_name':file_name,'file_size':file_size, 'file_date': file_upload_date})
        
        return file_name_size
                
        
    def save_document(self, user_id):
        pass

    def delete_document(self, user_id, document_id):
         # Check if the current file exists
        if os.path.exists(self.root_directory + user_id + "/" + document_id):
             # Remove the file
            os.remove(self.root_directory + user_id + "/" + document_id)
            

    def edit_document_name(self, user_id, old_name, new_name):
    
        old_file_full_path = self.root_directory + user_id + "/" + old_name
        new_file_full_path = self.root_directory + user_id + "/" + new_name

        # Check if the current file exists
        if os.path.exists(old_file_full_path):
            # Rename the file
            os.rename(old_file_full_path, new_file_full_path)

    def get_document_path(self, user_id, document_name):
        if os.path.exists(self.root_directory + user_id + "/" + document_name):
            return self.root_directory + user_id + "/" + document_name
        else:
            return False

    def file_system_exist(self, user_id):
        if os.path.exists(self.root_directory + user_id):
            pass
        else:
            os.makedirs(self.root_directory + user_id)  

    def convert_bytes(self, byte_size):
        # Define the units and their respective labels
        units = config.units

        # Start with the smallest unit (bytes) and convert
        unit_index = 0
        while byte_size >= 1024 and unit_index < len(units) - 1:
            byte_size /= 1024.0
            unit_index += 1

        # Format the result with up to two decimal places
        return f"{byte_size:.2f} {units[unit_index]}"

    def get_last_modified_date(self, file_path):

        stat = os.stat(file_path)
        file_last_date =  datetime.fromtimestamp(stat.st_mtime)
        formatted_date = file_last_date.strftime(config.date_time_format)

        return formatted_date
        