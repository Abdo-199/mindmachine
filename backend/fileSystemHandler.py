import os
import config
import logHandler
import ocrmypdf
import pikepdf
from datetime import datetime
from Neural_Search.PdfReader import pdf_to_docVec

class FileSystemHandler:
    
    def __init__(self, qdClient):
        self.document_directory = config.document_directory
        self.file_extension = config.file_extension
        self.qdClient = qdClient
        self.logger = logHandler.LogHandler(name="FileSystemHandler").get_logger()
        ocrmypdf.configure_logging(ocrmypdf.Verbosity.default)
        os.environ["TOKENIZERS_PARALLELISM"] = "false"

    def upload(self, user_id, files):
        """
        Uploads pdfs for a given user.
        This pdf is saved in the user's directory, if OCR is successful. 
        The OCR recognises text on the pdf, if the text is not editable.  

        Args:
            user_id (str): The ID of the user.
            files (list): A list of pdfs to be uploaded.

        Returns:
            list: A list of status indicating the success or failure of each file upload.
                  Each element in the list is a list containing the filename and a boolean
                  value indicating the upload status (True for success, False for failure).
        """
        self.file_system_exist(user_id=user_id)
        status_return = []
        for file in files:
            file_path = os.path.join(self.document_directory + user_id, file.filename)
            with open(file_path, "wb") as f:
                # saves original file to user directory
                f.write(file.file.read())
                try:              
                    self.encode_and_upload(file_path, user_id)
                    self.logger.debug(f"User {user_id} uploaded {file.filename}")
                    status_return.append([file.filename, True])
                except Exception as e:
                    # print(e)
                    self.logger.error(f"User {user_id} failed to upload {file.filename}: {e}")
                    status_return.append([file.filename, False])
                    self.delete_document(user_id, file.filename)
                    continue

        return status_return
    
    def encode_and_upload(self, file_path, user):
        # saves ocr file to temp directory
        filename = os.path.basename(file_path)
        temp_file_path = config.temp_pdf_directory + filename
        os.makedirs(config.temp_pdf_directory, exist_ok=True)
        # open pdf with pikepdf and remove restrictions
        pdf = pikepdf.open(file_path, password='')
        pdf.save(temp_file_path)
        # recognize text with ocrmypdf
        self.logger.debug(f"User {user} is running OCR on {filename}")
        ocrmypdf.ocr(
            temp_file_path,
            temp_file_path,
            output_type='pdf',
            skip_text=True,
            language=['deu', 'eng'],
            optimize=0,
            invalidate_digital_signatures=True
        )

        self.logger.debug(f"User {user} is encoding {filename}")
        # encode pdf to vectors
        docVec = pdf_to_docVec(file_path, self.qdClient.encoder)

        #check if there were paragraphs recognized
        if len(docVec.paras_vecs) <= 1 and docVec.paras_vecs[0]['paragraph'] == '':
            self.logger.error(f"User {user} failed to upload {filename}: No paragraphs recognized")
            raise Exception("No paragraphs recognized")  
        
        # save vectors to qdrant
        self.logger.debug(f"save {filename} vectors to qdrant")
        self.qdClient.add_docVec(user, docVec)

        # delete temp file
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

    def get_fs_for_user(self, user_id):

        file_name_size = []
        self.file_system_exist(user_id=user_id)

        # Only search for files with a certain extension, see file_extension in config.py
        files = [file for file in os.listdir(self.document_directory + user_id) if file.endswith(self.file_extension)]

        for file_name in files:

            file_path = os.path.join(self.document_directory + user_id, file_name)
            file_size = os.path.getsize(file_path)

            # Convert Bytes to Megabytes
            file_size = self.convert_bytes(file_size)

            file_upload_date = self.get_last_modified_date(file_path)

            # Frontend Format
            file_name_size.append({'file_name':file_name,'file_size':file_size, 'file_date': file_upload_date})
        
        return file_name_size
    
    def get_file_size_for_user(self, user_id):
        total_file_size = 0
        files = [file for file in os.listdir(self.document_directory + user_id) if file.endswith(self.file_extension)]
        for file in files:
            file_path = os.path.join(self.document_directory + user_id, file)
            file_size = os.path.getsize(file_path)
            total_file_size +=  file_size

        total_file_size = self.convert_bytes(total_file_size)
        return total_file_size
    
    def get_total_file_size_for_all_users(self):
        total_file_size = 0
        for user_folder in os.listdir(self.document_directory):
            user_folder_path = os.path.join(self.document_directory, user_folder)
            if os.path.isdir(user_folder_path):  # Check if it's a directory
                files = [file for file in os.listdir(user_folder_path) if file.endswith(self.file_extension)]
                for file in files:
                    file_path = os.path.join(user_folder_path, file)
                    file_size = os.path.getsize(file_path)
                    total_file_size += file_size

        total_file_size = self.convert_bytes(total_file_size)

        return total_file_size

    
                
        
    def save_document(self, user_id):
        pass

    def delete_document(self, user_id, document_id):
        self.logger.debug(f"Attempting to delete document {document_id} for user {user_id}")
        if os.path.exists(self.document_directory + user_id + "/" + document_id):
            os.remove(self.document_directory + user_id + "/" + document_id)
            self.qdClient.delete_doc(user_id, document_id)
            self.logger.info(f"Document {document_id} deleted for user {user_id}")
        else:
            self.logger.warning(f"Document {document_id} not found for user {user_id}")

    def edit_document_name(self, user_id, old_name, new_name):
        self.logger.debug(f"Attempting to rename document from {old_name} to {new_name} for user {user_id}")
        old_file_full_path = self.document_directory + user_id + "/" + old_name
        new_file_full_path = self.document_directory + user_id + "/" + new_name

        if os.path.exists(old_file_full_path):
            os.rename(old_file_full_path, new_file_full_path)
            self.logger.info(f"Document renamed from {old_name} to {new_name} for user {user_id}")
        else:
            self.logger.warning(f"Document {old_name} not found for user {user_id}")

    def get_document_path(self, user_id, document_name):
        self.logger.debug(f"Fetching document path for {document_name} for user {user_id}")
        path = self.document_directory + user_id + "/" + document_name
        if os.path.exists(path):
            self.logger.info(f"Document path for {document_name} retrieved for user {user_id}")
            return path
        else:
            self.logger.warning(f"Document {document_name} not found for user {user_id}")
            return False

    def file_system_exist(self, user_id):
        self.logger.debug(f"Checking if file system exists for user {user_id}")
        path = self.document_directory + user_id
        if not os.path.exists(path):
            os.makedirs(path)
            self.logger.info(f"File system created for user {user_id}")

    def convert_bytes(self, byte_size):
        # Define the units and their respective labels
        units = config.units

        # Start with the smallest unit (bytes) and convert
        self.logger.debug(f"Converting byte size: {byte_size}")
        unit_index = 0
        while byte_size >= 1024 and unit_index < len(units) - 1:
            byte_size /= 1024.0
            unit_index += 1
        # Format the result with up to two decimal places
        return f"{byte_size:.2f} {units[unit_index]}"

    def convert_bytes_to_gigabyte(self, byte_size):
    # Define the unit label
        unit = 'GB'

        # Convert bytes to gigabytes
        gigabytes = byte_size / (1024.0 ** 3)

        # Start with the smallest unit (bytes) and convert
        self.logger.debug(f"Converting byte size: {byte_size}")

        # Format the result with up to two decimal places
        return f"{gigabytes:.2f} {unit}"

    def get_last_modified_date(self, file_path):
        self.logger.debug(f"Getting last modified date for file: {file_path}")
        stat = os.stat(file_path)
        file_last_date =  datetime.fromtimestamp(stat.st_mtime)
        formatted_date = file_last_date.strftime(config.date_time_format)

        return formatted_date
        