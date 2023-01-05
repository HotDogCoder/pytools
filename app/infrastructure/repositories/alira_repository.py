from time import sleep

import constants
from app.application.repositories_interfaces.alira_repository_interface import AliraRepositoryInterface
from app.domain.models.alira import Alira
import requests, json

class AliraRepository(AliraRepositoryInterface):

    def __init__(self):
        super().__init__()

    def get_layouts_of_alira_page(self, alira: Alira):

        url = constants.API_UPLOAD_SCREENSHOT
        multiple_files = []

        return alira
