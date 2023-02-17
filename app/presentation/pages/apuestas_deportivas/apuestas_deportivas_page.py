from app.domain.models.apuestas_deportivas import ApuestasDeportivas
from app.presentation.controllers.apuestas_deportivas_controller import ApuestasDeportivasController


class ApuestasDeportivasPage:

    def __init__(self):
        pass

    @staticmethod
    def login_happy_ad(e):
        driver = 'Chrome'
        image_name_prefix = 'apuestas_deportivas_'

        apuestas_deportivas = ApuestasDeportivas(
            url="https://www.casinoatlanticcity.com/",
            image_name_prefix=image_name_prefix,
            driver=driver,
            apuestas_deportivas_helper=None,
            casino_helper             =None,

        )

        ADC = ApuestasDeportivasController()
        ADC.login_happy_ad(apuestas_deportivas=apuestas_deportivas)
        pass

    @staticmethod
    def login_happy_col(e):
        driver = 'Chrome'
        image_name_prefix = 'apuestas_deportivas_'

        apuestas_deportivas = ApuestasDeportivas(
            url="https://www.casinoatlanticcity.com/",
            image_name_prefix=image_name_prefix,
            driver=driver,
            apuestas_deportivas_helper=None,
            casino_helper=None
        )

        ADC = ApuestasDeportivasController()
        ADC.login_happy_col(apuestas_deportivas=apuestas_deportivas)
        pass

    @staticmethod
    def ad_promociones_1_0(e):
        driver = 'Chrome'
        image_name_prefix = 'apuestas_deportivas_'

        apuestas_deportivas = ApuestasDeportivas(
            url="https://www.casinoatlanticcity.com/",
            image_name_prefix=image_name_prefix,
            driver=driver,
            casino_helper=None,
            apuestas_deportivas_helper=None,
        )

        ADC = ApuestasDeportivasController()
        ADC.ad_promociones_1_0(apuestas_deportivas=apuestas_deportivas)
        pass

    @staticmethod
    def col_promociones_1_0(e):
        driver = 'Chrome'
        image_name_prefix = 'apuestas_deportivas_'

        apuestas_deportivas = ApuestasDeportivas(
            url="https://www.casinoatlanticcity.com/",
            image_name_prefix=image_name_prefix,
            driver=driver,
            apuestas_deportivas_helper=None,
            casino_helper=None
        )

        ADC = ApuestasDeportivasController()
        ADC.col_promociones_1_0(apuestas_deportivas=apuestas_deportivas)
        pass

    @staticmethod
    def visualizar_promocion_winner_de_winners(e):
        driver = 'Chrome'
        image_name_prefix = 'apuestas_deportivas_'

        apuestas_deportivas = ApuestasDeportivas(
            url="https://www.casinoatlanticcity.com/",
            image_name_prefix=image_name_prefix,
            driver=driver,
            apuestas_deportivas_helper=None,
            casino_helper=None
        )

        ADC = ApuestasDeportivasController()
        ADC.visualizar_promocion_winner_de_winners(apuestas_deportivas=apuestas_deportivas)
        pass

    @staticmethod
    def visualizar_depositos_col(e):
        driver = 'Chrome'
        image_name_prefix = 'apuestas_deportivas_'

        apuestas_deportivas = ApuestasDeportivas(
            url="https://www.casinoatlanticcity.com/",
            image_name_prefix=image_name_prefix,
            driver=driver,
            apuestas_deportivas_helper=None,
            casino_helper=None
        )

        ADC = ApuestasDeportivasController()
        ADC.visualizar_depositos_col(apuestas_deportivas=apuestas_deportivas)
        pass

    @staticmethod
    def visualizar_depositos_ad(e):
        driver = 'Chrome'
        image_name_prefix = 'apuestas_deportivas_'

        apuestas_deportivas = ApuestasDeportivas(
            url="https://www.casinoatlanticcity.com/",
            image_name_prefix=image_name_prefix,
            driver=driver,
            apuestas_deportivas_helper=None,
            casino_helper=None
        )

        ADC = ApuestasDeportivasController()
        ADC.visualizar_depositos_ad(apuestas_deportivas=apuestas_deportivas)
        pass