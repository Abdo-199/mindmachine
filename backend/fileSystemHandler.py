import os
import config
import ocrmypdf
import pikepdf
from datetime import datetime
from Neural_Search.PdfReader import pdf_to_docVec

class FileSystemHandler:
    
    def __init__(self, qdClient):
        self.document_directory = config.document_directory
        self.file_extension = config.file_extension
        self.qdClient = qdClient
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
                    # saves ocr file to temp directory
                    temp_file_path = config.temp_pdf_directory + file.filename
                    os.makedirs(config.temp_pdf_directory, exist_ok=True)
                    # open pdf with pikepdf and remove restrictions
                    pdf = pikepdf.open(file_path, password='')
                    pdf.save(temp_file_path)
                    # recognize text with ocrmypdf
                    ocrmypdf.ocr(
                        temp_file_path,
                        temp_file_path,
                        output_type='pdf',
                        skip_text=True,
                        language=['deu', 'eng'],
                        optimize=0,
                        invalidate_digital_signatures=True
                    )
                    # encode pdf to vectors
                    docVec = pdf_to_docVec(temp_file_path, self.qdClient.encoder)

                    #check if there were paragraphs recognized
                    if len(docVec.paras_vecs) <= 1 and docVec.paras_vecs[0]['paragraph'] == '':
                        raise Exception("No paragraphs recognized")   
                                     
                    # save vectors to qdrant
                    self.qdClient.add_docVec(user_id, docVec)
                    if os.path.exists(temp_file_path):
                        os.remove(temp_file_path)
                    status_return.append([file.filename, True])
                except Exception as e:
                    print(e)
                    status_return.append([file.filename, False])
                    self.delete_document(user_id, file.filename)
                    continue

        return status_return

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
                
        
    def save_document(self, user_id):
        pass

    def delete_document(self, user_id, document_id):
         # Check if the current file exists
        if os.path.exists(self.document_directory + user_id + "/" + document_id):
             # Remove the file
            os.remove(self.document_directory + user_id + "/" + document_id)
            self.qdClient.delete_doc(user_id, document_id)
            

    def edit_document_name(self, user_id, old_name, new_name):
    
        old_file_full_path = self.document_directory + user_id + "/" + old_name
        new_file_full_path = self.document_directory + user_id + "/" + new_name

        # Check if the current file exists
        if os.path.exists(old_file_full_path):
            # Rename the file
            os.rename(old_file_full_path, new_file_full_path)

    def get_document_path(self, user_id, document_name):
        if os.path.exists(self.document_directory + user_id + "/" + document_name):
            return self.document_directory + user_id + "/" + document_name
        else:
            return False

    def file_system_exist(self, user_id):
        if os.path.exists(self.document_directory + user_id):
            pass
        else:
            os.makedirs(self.document_directory + user_id)  

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
        