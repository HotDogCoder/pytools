from application.services.server_request_service import ServerRequestService
from domain.models.server_request import ServerRequest
from infrastructure.repositories.server_request_repository import ServerRequestRepository
from presentation.controllers.server_request_controller import ServerRequestController

SRR = ServerRequestRepository()
SRS = ServerRequestService(SRR)
SRC = ServerRequestController(SRS)

# print(SRC.insert_server_request(ServerRequest("POST", "SERVER", "WIN", 8000, "localhost")).method)
SRC.
