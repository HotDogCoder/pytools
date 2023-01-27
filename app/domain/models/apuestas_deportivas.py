from features.apuestas_deportivas.apuestas_deportivas_helper import ApuestasDeportivasHelper
from features.casino.casino_helper import CasinoHelper


class ApuestasDeportivas:

    def __init__(self, url, image_name_prefix, driver, casino_helper: CasinoHelper,
                 apuestas_deportivas_helper: ApuestasDeportivasHelper):
        self.url = url
        self.image_name_prefix = image_name_prefix
        self.driver = driver
        self.image_list = []
        self.data_list = []
        self.casino_helper = casino_helper
        self.apuestas_deportivas_helper = apuestas_deportivas_helper