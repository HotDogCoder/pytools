import sys
from core.config import constants
from datetime import datetime
import pytz
import logging

from app.domain import SftpParameter
from app.presentation.controllers.server_request_controller import ServerRequestController

logger = logging.getLogger(__name__)

# SRR = ServerRequestRepository()
# SRS = ServerRequestService(SRR)
SRC = ServerRequestController()

# print(SRC.insert_server_request(ServerRequest("POST", "SERVER", "WIN", 8000, "localhost")).method)
# SRC.get_server_request_files_data(ServerRequestFilter("2022-11-03", 'some text', 0, "POST", "SERVER"))

tz = pytz.timezone('America/Bogota')

parameters = sys.argv
print('----------------------------------------------------------------')
print('1 . parameters :', parameters)
# parameters.append('C:/Users/jhospinal/Documents/text.html')
parameters.append('no specific file')

try:

    local_file_path = sys.argv[1]

    if len(parameters) > 2:
        target_path = sys.argv[2]
    else:
        # target_path = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
        target_path = 'public_html'
        # PE280\llazo
    if len(parameters) > 3:
        directory_name = sys.argv[3]
    else:
        # target_path = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
        directory_name = datetime.now(tz).strftime('%d%m%Y')
        # directory_name = '04112022'

    print('2 . local path: ', local_file_path)
    print('3 . target path: ', target_path)
    print('4 . directory name: ', directory_name)
    print('5 . new file name: ', f"{target_path}/{directory_name}/secrets.json")

except IndexError as e:

    print('Error : Local file is missing check your command :')
    print('Example : python sftp_automatic_upload.py local_file_path target_path directory_name')
    print(e)

    pass

else:
    print('----------------------------------------------------------------')
    SRC.upload_file_into_external_folder(
        SftpParameter(
            constants.SFTP_HOST,
            constants.SFTP_PORT,
            constants.SFTP_USERNAME,
            constants.SFTP_PASSWORD,
            "",
            local_file_path,
            target_path,
            directory_name
        )
    )

# python sftp_automatic_upload.py 'C:/Users/jhospinal/Documents/secrets.json'
