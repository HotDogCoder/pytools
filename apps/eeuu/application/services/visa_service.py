from apps.eeuu.application.services_interfaces.visa_service_interface import VisaServiceInterface
from apps.eeuu.helpers.visa_helper import VisaHelper
from apps.eeuu.infrastructure.repositories.visa_repository import VisaRepository
from apps.eeuu.domain.models.visa_model import VisaModel
import pytz
from datetime import datetime
from core.domain.models.url import Url
from core.util.debug.trace_helper import TraceHelper
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.chrome.service import Service

class VisaService(VisaServiceInterface):
    def __init__(self):
        super().__init__()
        self.visa_repository = VisaRepository()

    def query(self, visa_model: VisaModel):
        return self.visa_repository.query(visa_model)
    def upload(self, visa_model: VisaModel):
        return self.visa_repository.upload(visa_model)
    def post(self, visa_model: VisaModel):
        return self.visa_repository.post(visa_model)
    def get(self, visa_model: VisaModel):
        try:
            driver = None
            if visa_model.driver == 'Chrome':
                chrome_options = ChromeOptions()
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
                # chrome_options.add_argument('--headless')
                chrome_options.add_argument('--disable-gpu')
                chrome_service = Service('/Users/Shared/chromedriver/chromedriver')
                driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
            elif visa_model.driver == 'Firefox':
                driver = webdriver.Firefox()
            elif visa_model.driver == 'Safari':
                driver = webdriver.Safari()
            elif visa_model.driver == 'Edge':
                driver = webdriver.Edge()
            tz = pytz.timezone('America/Bogota')
            directory_name = datetime.now(tz).strftime('%Y%m%d%H%M%S')
            visa_helper = VisaHelper(driver, visa_model=visa_model)
            visa_helper.login()
            if visa_model.task == 'schedule':
                visa_helper.schedule()
            elif visa_model.task == 'reschedule':
                visa_helper.reschedule()
            driver.close()
        except (UnicodeDecodeError, StopIteration) as e:
            print('error: ', e)
        return self.visa_repository.get(visa_model)
    def put(self, visa_model: VisaModel):
        return self.visa_repository.put(visa_model)
    def delete(self, visa_model: VisaModel):
        return self.visa_repository.delete(visa_model)
