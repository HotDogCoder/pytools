from application.services.server_request_service import ServerRequestService
from domain.models.server_request import ServerRequest
from domain.models.server_request_filter import ServerRequestFilter


class ServerRequestController:

    def __init__(self, server_request_service: ServerRequestService):
        self.server_request_service = server_request_service

    def insert_server_request(self, server_request: ServerRequest):
        return self.server_request_service.insert_server_request(server_request)

    def select_server_request(self, server_request_filter: ServerRequestFilter):
        pass

    def get_server_request_files_data(self, server_request_filter: ServerRequestFilter):
        return
