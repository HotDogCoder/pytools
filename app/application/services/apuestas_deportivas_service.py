import os
from time import sleep

import pytz
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from app.application.services_interfaces.apuestas_deportivas_service_interface import ApuestasDeportivasServiceInterface
from app.domain.models.apuestas_deportivas import ApuestasDeportivas
from app.infrastructure.repositories.apuestas_deportivas_repository import ApuestasDeportivasRepository

from core.domain.models.url import Url
from core.util.debug.trace_helper import TraceHelper
from features.apuestas_deportivas.apuestas_deportivas_helper import ApuestasDeportivasHelper


class ApuestasDeportivasService(ApuestasDeportivasServiceInterface):

    def __init__(self):
        super().__init__()
        self.apuestas_deportivas_repository = ApuestasDeportivasRepository()

    def login_happy_path(self, apuestas_deportivas: ApuestasDeportivas):
        """AQUI FUNCIONA EL SELENIUM"""
        try:
            driver = None

            if apuestas_deportivas.driver == 'Chrome':
                driver = webdriver.Chrome()
            elif apuestas_deportivas.driver == 'Firefox':
                driver = webdriver.Firefox()
            elif apuestas_deportivas.driver == 'Safari':
                driver = webdriver.Safari()
            elif apuestas_deportivas.driver == 'Edge':
                driver = webdriver.Edge()

            tz = pytz.timezone('America/Bogota')
            directory_name = datetime.now(tz).strftime('%Y%m%d%H%M%S')

            apuestas_deportivas.apuestas_deportivas_helper = ApuestasDeportivasHelper(driver, page=0)
            apuestas_deportivas.apuestas_deportivas_helper.login()

            apuestas_deportivas.apuestas_deportivas_helper.complete_id_alira()



        except (Exception, StopIteration) as e:

            print(f"Error : {apuestas_deportivas.apuestas_deportivas_helper.trace_helper.get_trace_str(e)}")

        return self.apuestas_deportivas_repository.login_happy_path(apuestas_deportivas)

    def visualizar_torneos(self, apuestas_deportivas: ApuestasDeportivas):

        try:
            driver = None

            if apuestas_deportivas.driver == 'Chrome':
                driver = webdriver.Chrome()
            elif apuestas_deportivas.driver == 'Firefox':
                driver = webdriver.Firefox()
            elif apuestas_deportivas.driver == 'Safari':
                driver = webdriver.Safari()
            elif apuestas_deportivas.driver == 'Edge':
                driver = webdriver.Edge()

            tz = pytz.timezone('America/Bogota')
            directory_name = datetime.now(tz).strftime('%Y%m%d%H%M%S')

            apuestas_deportivas.apuestas_deportivas_helper = ApuestasDeportivasHelper(driver, page=0)
            apuestas_deportivas.apuestas_deportivas_helper.login()
            apuestas_deportivas.apuestas_deportivas_helper.ingresar_promociones()
            apuestas_deportivas.apuestas_deportivas_helper.complete_id_alira()
            apuestas_deportivas.apuestas_deportivas_helper.bajar_cursor()

        except (Exception, StopIteration) as e:

            print(f"Error : {apuestas_deportivas.apuestas_deportivas_helper.trace_helper.get_trace_str(e)}")

        return self.apuestas_deportivas_repository.visualizar_torneos(apuestas_deportivas)