import logging
# change this to logging.DEBUG to see more information.
# change this to logging.INFO to see less information.
# change this to logging.WARNING to see only warnings.
min_log_level = logging.INFO

#root_directory = "./user/"
root_directory = "/usr/src/app/"

document_directory =  root_directory + "mm_docs/user/"

data_directory = root_directory + "data/"

log_directory = data_directory + "logs/"
log_file = log_directory + "log.txt"

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

max_search_history_per_user = 50  # Change as needed
max_disk_space = 53687091200.0 # equals 50 gigabyte in byte
user_max_disk_space = 1073741824.0 # equals 1 gigabyte in byte
logout_timer = 60.0 # value in minutes