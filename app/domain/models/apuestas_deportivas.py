from features.apuestas_deportivas.apuestas_deportivas_helper import ApuestasDeportivasHelper


class ApuestasDeportivas:

    def __init__(self, url, image_name_prefix, driver, apuestas_deportivas_helper: ApuestasDeportivasHelper):
        self.url = url
        self.image_name_prefix = image_name_prefix
        self.driver = driver
        self.image_list = []
        self.data_list = []
        self.apuestas_deportivas_helper = apuestas_deportivas_helper