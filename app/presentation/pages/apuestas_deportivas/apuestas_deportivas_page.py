from app.domain.models.apuestas_deportivas import ApuestasDeportivas
from app.presentation.controllers.apuestas_deportivas_controller import ApuestasDeportivasController


class ApuestasDeportivasPage:

    def __init__(self):
        pass

    @staticmethod
    def login_happy_path(e):
        driver = 'Chrome'
        image_name_prefix = 'apuestas_deportivas_'

        apuestas_deportivas = ApuestasDeportivas(
            url="https://atlantic:viQ[3UJ*Rk*Q1zC@atlanticcity.pre.tecnalis.com/",
            image_name_prefix=image_name_prefix,
            driver=driver,
            apuestas_deportivas_helper=None
        )

        ADC = ApuestasDeportivasController()
        ADC.login_happy_path(apuestas_deportivas=apuestas_deportivas)
        pass

    @staticmethod
    def visualizar_torneos(e):
        driver = 'Chrome'
        image_name_prefix = 'apuestas_deportivas_'

        apuestas_deportivas = ApuestasDeportivas(
            url="https://atlantic:viQ[3UJ*Rk*Q1zC@atlanticcity.pre.tecnalis.com/",
            image_name_prefix=image_name_prefix,
            driver=driver,
            apuestas_deportivas_helper=None
        )

        ADC = ApuestasDeportivasController()
        ADC.visualizar_torneos(apuestas_deportivas=apuestas_deportivas)
        pass
    