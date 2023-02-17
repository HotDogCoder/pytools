from app.application.services.apuestas_deportivas_service import ApuestasDeportivasService
from app.domain.models.apuestas_deportivas import ApuestasDeportivas


class ApuestasDeportivasController:

    def __init__(self):
        self.apuestas_deportivas_service = ApuestasDeportivasService()

    def login_happy_ad(self, apuestas_deportivas: ApuestasDeportivas):
        return self.apuestas_deportivas_service.login_happy_ad(apuestas_deportivas)

    def login_happy_col(self, apuestas_deportivas: ApuestasDeportivas):
        return self.apuestas_deportivas_service.login_happy_col(apuestas_deportivas)
    def ad_promociones_1_0(self, apuestas_deportivas: ApuestasDeportivas):
        return self.apuestas_deportivas_service.ad_promociones_1_0(apuestas_deportivas)
    def col_promociones_1_0(self, apuestas_deportivas: ApuestasDeportivas):
        return self.apuestas_deportivas_service.col_promociones_1_0(apuestas_deportivas)
    def visualizar_promocion_winner_de_winners(self, apuestas_deportivas: ApuestasDeportivas):
        return self.apuestas_deportivas_service.visualizar_promocion_winner_de_winners(apuestas_deportivas)

    def visualizar_depositos_col(self, apuestas_deportivas: ApuestasDeportivas):
        return self.apuestas_deportivas_service.visualizar_depositos_col(apuestas_deportivas)

    def visualizar_depositos_ad(self, apuestas_deportivas: ApuestasDeportivas):
        return self.apuestas_deportivas_service.visualizar_depositos_ad(apuestas_deportivas)