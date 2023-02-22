import os
from time import sleep

import pytz
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from app.application.services_interfaces.apuestas_deportivas_service_interface import ApuestasDeportivasServiceInterface
from app.domain.models.apuestas_deportivas import ApuestasDeportivas
from app.domain.models.promocion import Promocion
from app.infrastructure.repositories.apuestas_deportivas_repository import ApuestasDeportivasRepository

from core.domain.models.url import Url
from core.util.debug.trace_helper import TraceHelper
from features.apuestas_deportivas.apuestas_deportivas_helper import ApuestasDeportivasHelper
from features.casino.casino_helper import CasinoHelper


class ApuestasDeportivasService(ApuestasDeportivasServiceInterface):

    def __init__(self):
        super().__init__()
        self.apuestas_deportivas_repository = ApuestasDeportivasRepository()

    def login_happy_ad(self, apuestas_deportivas: ApuestasDeportivas):
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

        return self.apuestas_deportivas_repository.login_happy_ad(apuestas_deportivas)

    def login_happy_col(self, apuestas_deportivas: ApuestasDeportivas):
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


        except (Exception, StopIteration) as e:

            print(f"Error : {apuestas_deportivas.apuestas_deportivas_helper.trace_helper.get_trace_str(e)}")

        return self.apuestas_deportivas_repository.login_happy_col(apuestas_deportivas)

    def ad_promociones_1_0(self, apuestas_deportivas: ApuestasDeportivas):
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

            orden_promos = [

                Promocion(4, "TORNEO_DE_VERANO", 1),  ("IZQUIERDA LUGAR DEL TORNEO ,DERECHA EL NIVEL")
                Promocion(2, "TORNEO_DE_VERANO", 2),
                Promocion(1, "TORNEO_DE_VERANO", 3),
                Promocion(1, "TORNEO_DE_VERANO", 5),
                Promocion(1, "TORNEO_DE_VERANO", 6),
                Promocion(1, "TORNEO_DE_VERANO", 7),
                Promocion(1, "TORNEO_DE_VERANO", 8),
                Promocion(1, "TORNEO_DE_VERANO", 9),
                Promocion(1, "TORNEO_DE_VERANO", 0),


                Promocion(4, "TORNEO_DE_VERANO", 1),
                Promocion(2, "TORNEO_DE_VERANO", 2),
                Promocion(1, "TORNEO_DE_VERANO", 3),
                Promocion(1, "TORNEO_DE_VERANO", 5),
                Promocion(1, "TORNEO_DE_VERANO", 6),
                Promocion(1, "TORNEO_DE_VERANO", 7),
                Promocion(1, "TORNEO_DE_VERANO", 8),
                Promocion(1, "TORNEO_DE_VERANO", 9),
                Promocion(1, "TORNEO_DE_VERANO", 0),

                Promocion(4, "TORNEO_DE_VERANO", 1),
                Promocion(2, "TORNEO_DE_VERANO", 2),
                Promocion(1, "TORNEO_DE_VERANO", 3),
                Promocion(1, "TORNEO_DE_VERANO", 5),
                Promocion(1, "TORNEO_DE_VERANO", 6),
                Promocion(1, "TORNEO_DE_VERANO", 7),
                Promocion(1, "TORNEO_DE_VERANO", 8),
                Promocion(1, "TORNEO_DE_VERANO", 9),
                Promocion(1, "TORNEO_DE_VERANO", 0),

                Promocion(4, "TORNEO_DE_VERANO", 1),
                Promocion(2, "TORNEO_DE_VERANO", 2),
                Promocion(1, "TORNEO_DE_VERANO", 3),
                Promocion(1, "TORNEO_DE_VERANO", 5),
                Promocion(1, "TORNEO_DE_VERANO", 6),
                Promocion(1, "TORNEO_DE_VERANO", 7),
                Promocion(1, "TORNEO_DE_VERANO", 8),
                Promocion(1, "TORNEO_DE_VERANO", 9),
                Promocion(1, "TORNEO_DE_VERANO", 0),

                Promocion(4, "TORNEO_DE_VERANO", 1),
                Promocion(2, "TORNEO_DE_VERANO", 2),
                Promocion(1, "TORNEO_DE_VERANO", 3),
                Promocion(1, "TORNEO_DE_VERANO", 5),
                Promocion(1, "TORNEO_DE_VERANO", 6),
                Promocion(1, "TORNEO_DE_VERANO", 7),
                Promocion(1, "TORNEO_DE_VERANO", 8),
                Promocion(1, "TORNEO_DE_VERANO", 9),
                Promocion(1, "TORNEO_DE_VERANO", 0),

                Promocion(4, "TORNEO_DE_VERANO", 1),
                Promocion(2, "TORNEO_DE_VERANO", 2),
                Promocion(1, "TORNEO_DE_VERANO", 3),
                Promocion(1, "TORNEO_DE_VERANO", 5),
                Promocion(1, "TORNEO_DE_VERANO", 6),
                Promocion(1, "TORNEO_DE_VERANO", 7),
                Promocion(1, "TORNEO_DE_VERANO", 8),
                Promocion(1, "TORNEO_DE_VERANO", 9),
                Promocion(1, "TORNEO_DE_VERANO", 0),

            ]
            for index, orden_promo in enumerate(orden_promos):
                apuestas_deportivas.casino_helper.visualizar_orden_de_promociones(orden_promo, index)
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

        return self.apuestas_deportivas_repository.ad_promociones_1_0(apuestas_deportivas)

    def col_promociones_1_0(self, apuestas_deportivas: ApuestasDeportivas):
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
            orden_promos = [

                "TOP_100",
                "WINNER_DE_WINNERS",

            ]
            for orden_promo in orden_promos:
                apuestas_deportivas.casino_helper.visualizar_orden_de_promociones(orden_promo)
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

        return self.apuestas_deportivas_repository.col_promociones_1_0(apuestas_deportivas)

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

        return self.apuestas_deportivas_repository.visualizar_promocion_winner_de_winners(apuestas_deportivas)

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
            apuestas_deportivas.casino_helper.depositar_col()
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

            apuestas_deportivas.casino_helper.depositar_col()

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

        return self.apuestas_deportivas_repository.visualizar_depositos_col(apuestas_deportivas)

    def visualizar_depositos_ad(self, apuestas_deportivas: ApuestasDeportivas):
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








        except (Exception, StopIteration) as e:

            print(f"Error : {apuestas_deportivas.apuestas_deportivas_helper.trace_helper.get_trace_str(e)}")

        return self.apuestas_deportivas_repository.visualizar_depositos_ad(apuestas_deportivas)

