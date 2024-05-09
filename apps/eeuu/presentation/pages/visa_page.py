from apps.eeuu.domain.models.visa_model import VisaModel
from apps.eeuu.presentation.controllers.visa_controller import VisaController
import flet as ft

class VisaPage():

    def __init__(self):
        pass

    @staticmethod
    def schedule(e):
        driver = 'Chrome'
        image_name_prefix = 'alira_'

        visa_model = VisaModel(
            url="https://ais.usvisa-info.com/es-pe/niv/users/sign_in",
            image_name_prefix=image_name_prefix,
            driver=driver,
            visa_helper=None,
            task='schedule'
        )

        VC = VisaController()
        VC.get(visa_model=visa_model)
        pass

    @staticmethod
    def reschedule(e):
        driver = 'Chrome'
        image_name_prefix = 'alira_'

        visa_model = VisaModel(
            url="https://ais.usvisa-info.com/es-pe/niv/users/sign_in",
            image_name_prefix=image_name_prefix,
            driver=driver,
            visa_helper=None,
            task='reschedule'
        )

        VC = VisaController()
        VC.get(visa_model=visa_model)
        pass