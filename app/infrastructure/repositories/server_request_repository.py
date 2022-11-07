import os
import numpy as np
import pysftp

from app.application.repositories_interfaces.server_request_repository_interface import ServerRequestRepositoryInterface
from app.domain.models.server_request import ServerRequest
from app.domain.models.server_request_filter import ServerRequestFilter
from app.domain.models.sftp_parameter import SftpParameter


class ServerRequestRepository(ServerRequestRepositoryInterface):
    def __init__(self):
        super().__init__()

    def insert_server_request(self, server_request: ServerRequest):
        return server_request

    def select_server_request(self, server_request_filter: ServerRequestFilter):
        pass

    def get_server_request_files_data(self, server_request_filter: ServerRequestFilter):
        current_directory = os.getcwd()
        print(current_directory)

        return
        raw_line = []
        matriz_line = []
        with open(current_directory + '/py_app/u_ex210816.log', encoding='utf8') as f:
            for line in f:
                str_line = line.strip()
                str_line_array = str_line.split(' ')
                # print(str_line_array)
                raw_line.append(line.strip())
                matriz_line.append([str for str in str_line_array])

        num_raw_line = np.array(raw_line)
        num_matriz_line = np.array(matriz_line)
        # print(raw_line)
        return num_matriz_line

    def upload_file_into_external_folder(self, sftp_parameter: SftpParameter):
        open('//HOST/share/path/to/file')
        print('hola')
        return False

        with pysftp.Connection(
                host=sftp_parameter.host,
                username=sftp_parameter.user_name,
                password=sftp_parameter.password,
                port=sftp_parameter.port
        ) as sftp:
            print("sftp connection success")
            sftp.cwd(sftp_parameter.target_path)
            fnames = sftp.listdir()
            print('old file list: ', fnames)
            if sftp_parameter.directory_name in fnames:
                print('directory maybe exist')
                if not sftp.isdir('test'):
                    print('warning there is some file with the same name of the target folder')
                    print('creating directory anyway')
                    sftp.rename(sftp_parameter.directory_name, f"{sftp_parameter.directory_name}_backup")
                    sftp.mkdir(sftp_parameter.directory_name)
                else:
                    print('directory exist the file will be created or replaced there')
            else:
                sftp.mkdir(sftp_parameter.directory_name)
                print(sftp_parameter.directory_name)

            try:
                sftp.put(
                    sftp_parameter.local_file_path,
                    preserve_mtime=True,
                    remotepath=f"/{sftp_parameter.target_path}/{sftp_parameter.directory_name}/xd.html"
                )
            except FileNotFoundError as e:
                print('check if your local file exists :')
                print(e)
            else:
                fnames = sftp.listdir()
                print('new file list :', fnames)
        print('----------------------------------------------------------------')
        return False
