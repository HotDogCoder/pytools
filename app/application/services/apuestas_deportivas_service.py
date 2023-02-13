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
from features.casino.casino_helper import CasinoHelper


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

            apuestas_deportivas.apuestas_deportivas_helper = ApuestasDeportivasHelper(driver, page=0,
                                                                                      url=apuestas_deportivas.url)
            apuestas_deportivas.casino_helper = CasinoHelper(driver, page=0, url=apuestas_deportivas.url)
            apuestas_deportivas.apuestas_deportivas_helper.login_ad()


            apuestas_deportivas.casino_helper.usuario_password_nivel(1)


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

            apuestas_deportivas.apuestas_deportivas_helper = ApuestasDeportivasHelper(driver, page=0,
                                                                                      url=apuestas_deportivas.url)

            apuestas_deportivas.casino_helper = CasinoHelper(driver, page=0, url=apuestas_deportivas.url)
            apuestas_deportivas.casino_helper.login_col()

            apuestas_deportivas.casino_helper.usuario_password_nivel(1)



        except (Exception, StopIteration) as e:

            print(f"Error : {apuestas_deportivas.apuestas_deportivas_helper.trace_helper.get_trace_str(e)}")

        return self.apuestas_deportivas_repository.visualizar_torneos(apuestas_deportivas)

    def visualizar_promociones_pro(self, apuestas_deportivas: ApuestasDeportivas):
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

            apuestas_deportivas.apuestas_deportivas_helper = ApuestasDeportivasHelper(driver, page=0,
                                                                                      url=apuestas_deportivas.url)
            apuestas_deportivas.casino_helper = CasinoHelper(driver, page=0, url=apuestas_deportivas.url)

            apuestas_deportivas.apuestas_deportivas_helper.login_ad()
            apuestas_deportivas.casino_helper.usuario_password_nivel(1)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()
            apuestas_deportivas.casino_helper.ingresar_menu()
            apuestas_deportivas.casino_helper.ingresar_promociones()
            apuestas_deportivas.casino_helper.bajar_cursor(x=0,y=500)
            apuestas_deportivas.apuestas_deportivas_helper.cerrar_sesión_ad()

            apuestas_deportivas.casino_helper.iniciar_sesion()
            apuestas_deportivas.casino_helper.usuario_password_nivel(2)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()
            apuestas_deportivas.casino_helper.ingresar_menu()
            apuestas_deportivas.casino_helper.ingresar_promociones()
            apuestas_deportivas.casino_helper.bajar_cursor(x=0,y=500)
            apuestas_deportivas.apuestas_deportivas_helper.cerrar_sesión_ad()

            apuestas_deportivas.casino_helper.iniciar_sesion()
            apuestas_deportivas.casino_helper.usuario_password_nivel(3)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()
            apuestas_deportivas.casino_helper.ingresar_menu()
            apuestas_deportivas.casino_helper.ingresar_promociones()
            apuestas_deportivas.casino_helper.bajar_cursor(x=0,y=500)
            apuestas_deportivas.apuestas_deportivas_helper.cerrar_sesión_ad()

            apuestas_deportivas.casino_helper.iniciar_sesion()
            apuestas_deportivas.casino_helper.usuario_password_nivel(4)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()
            apuestas_deportivas.casino_helper.ingresar_menu()
            apuestas_deportivas.casino_helper.ingresar_promociones()
            apuestas_deportivas.casino_helper.bajar_cursor(x=0,y=500)
            apuestas_deportivas.apuestas_deportivas_helper.cerrar_sesión_ad()

            apuestas_deportivas.casino_helper.iniciar_sesion()
            apuestas_deportivas.casino_helper.usuario_password_nivel(5)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()
            apuestas_deportivas.casino_helper.ingresar_menu()
            apuestas_deportivas.casino_helper.ingresar_promociones()
            apuestas_deportivas.casino_helper.bajar_cursor(x=0,y=500)
            apuestas_deportivas.apuestas_deportivas_helper.cerrar_sesión_ad()

            apuestas_deportivas.casino_helper.iniciar_sesion()
            apuestas_deportivas.casino_helper.usuario_password_nivel(6)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()
            apuestas_deportivas.casino_helper.ingresar_menu()
            apuestas_deportivas.casino_helper.ingresar_promociones()
            apuestas_deportivas.casino_helper.bajar_cursor(x=0,y=500)
            apuestas_deportivas.apuestas_deportivas_helper.cerrar_sesión_ad()

            apuestas_deportivas.casino_helper.iniciar_sesion()
            apuestas_deportivas.casino_helper.usuario_password_nivel(7)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()
            apuestas_deportivas.casino_helper.ingresar_menu()
            apuestas_deportivas.casino_helper.ingresar_promociones()
            apuestas_deportivas.casino_helper.bajar_cursor(x=0,y=500)
            apuestas_deportivas.apuestas_deportivas_helper.cerrar_sesión_ad()

            apuestas_deportivas.casino_helper.iniciar_sesion()
            apuestas_deportivas.casino_helper.usuario_password_nivel(8)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()
            apuestas_deportivas.casino_helper.ingresar_menu()
            apuestas_deportivas.casino_helper.ingresar_promociones()
            apuestas_deportivas.casino_helper.bajar_cursor(x=0,y=500)
            apuestas_deportivas.apuestas_deportivas_helper.cerrar_sesión_ad()

            apuestas_deportivas.casino_helper.iniciar_sesion()
            apuestas_deportivas.casino_helper.usuario_password_nivel(9)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()
            apuestas_deportivas.casino_helper.ingresar_menu()
            apuestas_deportivas.casino_helper.ingresar_promociones()
            apuestas_deportivas.casino_helper.bajar_cursor(x=0,y=500)
            apuestas_deportivas.apuestas_deportivas_helper.cerrar_sesión_ad()

            apuestas_deportivas.casino_helper.iniciar_sesion()
            apuestas_deportivas.casino_helper.usuario_password_nivel(0)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()
            apuestas_deportivas.casino_helper.ingresar_menu()
            apuestas_deportivas.casino_helper.ingresar_promociones()
            apuestas_deportivas.casino_helper.bajar_cursor(x=0,y=500)
            apuestas_deportivas.apuestas_deportivas_helper.cerrar_sesión_ad()

        except (Exception, StopIteration) as e:

            print(f"Error : {apuestas_deportivas.apuestas_deportivas_helper.trace_helper.get_trace_str(e)}")

        return self.apuestas_deportivas_repository.login_happy_path(apuestas_deportivas)

    def col_promociones(self, apuestas_deportivas: ApuestasDeportivas):
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

            apuestas_deportivas.apuestas_deportivas_helper = ApuestasDeportivasHelper(driver, page=0,
                                                                                      url=apuestas_deportivas.url)
            apuestas_deportivas.casino_helper = CasinoHelper(driver, page=0, url=apuestas_deportivas.url)

            apuestas_deportivas.casino_helper.login_col()
            apuestas_deportivas.casino_helper.usuario_password_nivel(1)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()
            apuestas_deportivas.casino_helper.ingresar_menu()
            apuestas_deportivas.casino_helper.ingresar_promociones()
            apuestas_deportivas.casino_helper.bajar_cursor(x=0,y=500)
            apuestas_deportivas.casino_helper.cerrar_sesión_col()

            apuestas_deportivas.casino_helper.iniciar_sesion()
            apuestas_deportivas.casino_helper.usuario_password_nivel(2)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()
            apuestas_deportivas.casino_helper.ingresar_menu()
            apuestas_deportivas.casino_helper.ingresar_promociones()
            apuestas_deportivas.casino_helper.bajar_cursor(x=0,y=500)
            apuestas_deportivas.casino_helper.cerrar_sesión_col()

            apuestas_deportivas.casino_helper.iniciar_sesion()
            apuestas_deportivas.casino_helper.usuario_password_nivel(3)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()
            apuestas_deportivas.casino_helper.ingresar_menu()
            apuestas_deportivas.casino_helper.ingresar_promociones()
            apuestas_deportivas.casino_helper.bajar_cursor(x=0,y=500)
            apuestas_deportivas.casino_helper.cerrar_sesión_col()

            apuestas_deportivas.casino_helper.iniciar_sesion()
            apuestas_deportivas.casino_helper.usuario_password_nivel(4)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()
            apuestas_deportivas.casino_helper.ingresar_menu()
            apuestas_deportivas.casino_helper.ingresar_promociones()
            apuestas_deportivas.casino_helper.bajar_cursor(x=0,y=500)
            apuestas_deportivas.casino_helper.cerrar_sesión_col()

            apuestas_deportivas.casino_helper.iniciar_sesion()
            apuestas_deportivas.casino_helper.usuario_password_nivel(5)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()
            apuestas_deportivas.casino_helper.ingresar_menu()
            apuestas_deportivas.casino_helper.ingresar_promociones()
            apuestas_deportivas.casino_helper.bajar_cursor(x=0,y=500)
            apuestas_deportivas.casino_helper.cerrar_sesión_col()

            apuestas_deportivas.casino_helper.iniciar_sesion()
            apuestas_deportivas.casino_helper.usuario_password_nivel(6)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()
            apuestas_deportivas.casino_helper.ingresar_menu()
            apuestas_deportivas.casino_helper.ingresar_promociones()
            apuestas_deportivas.casino_helper.bajar_cursor(x=0,y=500)
            apuestas_deportivas.casino_helper.cerrar_sesión_col()

            apuestas_deportivas.casino_helper.iniciar_sesion()
            apuestas_deportivas.casino_helper.usuario_password_nivel(7)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()
            apuestas_deportivas.casino_helper.ingresar_menu()
            apuestas_deportivas.casino_helper.ingresar_promociones()
            apuestas_deportivas.casino_helper.bajar_cursor(x=0,y=500)
            apuestas_deportivas.casino_helper.cerrar_sesión_col()

            apuestas_deportivas.casino_helper.iniciar_sesion()
            apuestas_deportivas.casino_helper.usuario_password_nivel(8)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()
            apuestas_deportivas.casino_helper.ingresar_menu()
            apuestas_deportivas.casino_helper.ingresar_promociones()
            apuestas_deportivas.casino_helper.bajar_cursor(x=0,y=500)
            apuestas_deportivas.casino_helper.cerrar_sesión_col()

            apuestas_deportivas.casino_helper.iniciar_sesion()
            apuestas_deportivas.casino_helper.usuario_password_nivel(9)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()
            apuestas_deportivas.casino_helper.ingresar_menu()
            apuestas_deportivas.casino_helper.ingresar_promociones()
            apuestas_deportivas.casino_helper.bajar_cursor(x=0,y=500)
            apuestas_deportivas.casino_helper.cerrar_sesión_col()

            apuestas_deportivas.casino_helper.iniciar_sesion()
            apuestas_deportivas.casino_helper.usuario_password_nivel(0)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()
            apuestas_deportivas.casino_helper.ingresar_menu()
            apuestas_deportivas.casino_helper.ingresar_promociones()
            apuestas_deportivas.casino_helper.bajar_cursor(x=0,y=500)
            apuestas_deportivas.casino_helper.cerrar_sesión_col()

        except (Exception, StopIteration) as e:

            print(f"Error : {apuestas_deportivas.apuestas_deportivas_helper.trace_helper.get_trace_str(e)}")

        return self.apuestas_deportivas_repository.login_happy_path(apuestas_deportivas)

    def visualizar_promocion_winner_de_winners(self, apuestas_deportivas: ApuestasDeportivas):
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

            apuestas_deportivas.apuestas_deportivas_helper = ApuestasDeportivasHelper(driver, page=0,
                                                                                      url=apuestas_deportivas.url)
            apuestas_deportivas.casino_helper = CasinoHelper(driver, page=0, url=apuestas_deportivas.url)
            apuestas_deportivas.casino_helper.login_col()
            apuestas_deportivas.casino_helper.usuario_password_nivel(1)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()

            #apuestas_deportivas.casino_helper.ingresar_menu()
            #apuestas_deportivas.casino_helper.ingresar_promociones()
            #apuestas_deportivas.casino_helper.bajar_cursor(x=0, y=500)
            #apuestas_deportivas.casino_helper.seleccionar_promocion(0)







        except (Exception, StopIteration) as e:

            print(f"Error : {apuestas_deportivas.apuestas_deportivas_helper.trace_helper.get_trace_str(e)}")

        return self.apuestas_deportivas_repository.login_happy_path(apuestas_deportivas)

    def visualizar_depositos_col(self, apuestas_deportivas: ApuestasDeportivas):
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

            apuestas_deportivas.apuestas_deportivas_helper = ApuestasDeportivasHelper(driver, page=0,
                                                                                      url=apuestas_deportivas.url)
            apuestas_deportivas.casino_helper = CasinoHelper(driver, page=0, url=apuestas_deportivas.url)
            apuestas_deportivas.casino_helper.login_col()
            apuestas_deportivas.casino_helper.usuario_password_nivel(1)
            apuestas_deportivas.casino_helper.saltar_promoción_verano()
            apuestas_deportivas.casino_helper.depositar()
            forma_pagos =[

                "KASHIO",
                "INTERBANK",
                "SAFETYPAY",
                "VISA",
                "PAGOEFECTIVO",
                "PAGOQR",
            ]
            for forma_pago in forma_pagos:
                apuestas_deportivas.casino_helper.visualizar_todo_los_depositos_internet(forma_pago)

            apuestas_deportivas.casino_helper.depositar()

            forma_pagos = [

                "KASHIO",
                "INTERBANK",
                "SAFETYPAY",
                "PAGOEFECTIVO",
                "CAJEROATLANTIC",
            ]
            for forma_pago in forma_pagos:
                apuestas_deportivas.casino_helper.visualizar_todo_los_depositos_presencial(forma_pago)

            apuestas_deportivas.casino_helper.seleccionar_promocion(0)









        except (Exception, StopIteration) as e:

            print(f"Error : {apuestas_deportivas.apuestas_deportivas_helper.trace_helper.get_trace_str(e)}")

        return self.apuestas_deportivas_repository.login_happy_path(apuestas_deportivas)