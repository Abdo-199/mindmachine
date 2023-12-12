#root_directory = "./user/"
root_directory = "/usr/src/app/"

document_directory =  root_directory + "mm_docs/user/"

data_directory = root_directory + "data/"

database_name = "userid_search_history_admin.db"

#'/home/mindmachine/user/'
file_extension = '.pdf'

ldap_server = 'ldap://login-dc-01.login.htw-berlin.de'
base_dn = 'dc=login,dc=htw-berlin,dc=de'

qdrant_host = 'qdrant'
qdrant_port = 6333

date_time_format = '%d.%m.%Y'
units = ['B', 'KB', 'MB', 'GB', 'TB']

temp_pdf_directory = '/usr/src/app/data/temp_pdf/'