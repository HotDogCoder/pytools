from abc import ABC, abstractmethod

from app.domain.models.alira import Alira


class AliraServiceInterface(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_layouts_of_alira_page(self, alira: Alira):
        return alira

