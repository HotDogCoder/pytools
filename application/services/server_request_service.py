from application.services_interfaces.server_request_service_interface import ServerRequestServiceInterface
from domain.models.server_request import ServerRequest
from domain.models.server_request_filter import ServerRequestFilter
from infrastructure.repositories.server_request_repository import ServerRequestRepository


class ServerRequestService(ServerRequestServiceInterface):
    def __init__(self, server_request_repository: ServerRequestRepository):
        super().__init__()
        self.server_request_repository = server_request_repository

    def insert_server_request(self, server_request: ServerRequest):
        return self.server_request_repository.insert_server_request(server_request)

    def select_server_request(self, server_request_filter: ServerRequestFilter):
        return self.server_request_repository.get_server_request_files_data(server_request_filter)

    def get_server_request_files_data(self, server_request_filter: ServerRequestFilter):
        return self.server_request_repository.get_server_request_files_data(server_request_filter)

