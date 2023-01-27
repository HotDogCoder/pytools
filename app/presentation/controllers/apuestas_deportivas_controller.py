from app.application.services.apuestas_deportivas_service import ApuestasDeportivasService
from app.domain.models.apuestas_deportivas import ApuestasDeportivas


class ApuestasDeportivasController:

    def __init__(self):
        self.apuestas_deportivas_service = ApuestasDeportivasService()

    def login_happy_path(self, apuestas_deportivas: ApuestasDeportivas):
        return self.apuestas_deportivas_service.login_happy_path(apuestas_deportivas)

    def visualizar_torneos(self, apuestas_deportivas: ApuestasDeportivas):
        return self.apuestas_deportivas_service.visualizar_torneos(apuestas_deportivas)
    def visualizar_promociones_pro(self, apuestas_deportivas: ApuestasDeportivas):
        return self.apuestas_deportivas_service.visualizar_promociones_pro(apuestas_deportivas)
    def col_promociones(self, apuestas_deportivas: ApuestasDeportivas):
        return self.apuestas_deportivas_service.col_promociones(apuestas_deportivas)