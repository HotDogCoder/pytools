from abc import ABC, abstractmethod

from app.domain.models.server_request import ServerRequest
from app.domain import ServerRequestFilter
from app.domain.models.sftp_parameter import SftpParameter


class ServerRequestRepositoryInterface(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def insert_server_request(self, server_request: ServerRequest):
        pass

    @abstractmethod
    def select_server_request(self, server_request_filter: ServerRequestFilter):
        pass

    @abstractmethod
    def get_server_request_files_data(self, server_request_filter: ServerRequestFilter):
        pass

    @abstractmethod
    def upload_file_into_external_folder(self, sftp_parameter: SftpParameter):
        pass
