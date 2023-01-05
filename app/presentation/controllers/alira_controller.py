from app.application.services.alira_service import AliraService
from app.domain.models.alira import Alira


class AliraController:

    def __init__(self):
        self.alira_service = AliraService()

    def get_layouts_of_alira_page(self, alira: Alira):
        return self.alira_service.get_layouts_of_alira_page(alira)
