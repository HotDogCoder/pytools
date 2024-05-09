from apps.eeuu.helpers.visa_helper import VisaHelper


class VisaModel:
    def __init__(
            self, 
            url, 
            image_name_prefix,
            driver, 
            task='schedule',
            email=None,
            password=None,
            is_schedule=False,
            intent_limit_input=None
        ):
        self.url = url
        self.image_name_prefix = image_name_prefix
        self.driver = driver
        self.image_list = []
        self.data_list = []
        self.task = task
        self.email = email
        self.password = password
        self.is_schedule = is_schedule
        self.intent_limit_input = intent_limit_input
        self.date = ""
        self.time = ""
        self.result = False


