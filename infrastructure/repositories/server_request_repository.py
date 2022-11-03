import os
import numpy as np
from application.repositories_interfaces.server_request_repository_interface import ServerRequestRepositoryInterface
from domain.models.server_request import ServerRequest
from domain.models.server_request_filter import ServerRequestFilter


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
