import os
from time import sleep

import pytz
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from app.application.services_interfaces.alira_service_interface import AliraServiceInterface
from app.domain.models.alira import Alira
from app.infrastructure.repositories.alira_repository import AliraRepository

from core.domain.models.url import Url
from features.alira.alira_helper import AliraHelper


class AliraService(AliraServiceInterface):

    def __init__(self):
        super().__init__()
        self.alira_repository = AliraRepository()

    def set_seo_parameters_per_page(self, alira: Alira):

        try:
            driver = None

            if alira.driver == 'Chrome':
                driver = webdriver.Chrome()
            elif alira.driver == 'Firefox':
                driver = webdriver.Firefox()
            elif alira.driver == 'Safari':
                driver = webdriver.Safari()
            elif alira.driver == 'Edge':
                driver = webdriver.Edge()

            tz = pytz.timezone('America/Bogota')
            directory_name = datetime.now(tz).strftime('%Y%m%d%H%M%S')
            driver.maximize_window()
            driver.get(alira.url)

            target_user = driver.find_element(By.ID, "alias")
            target_password = driver.find_element(By.ID, "password")
            target_submit = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-success.btn-block")

            target_user.send_keys("rterrones")
            target_password.send_keys("P@ssw0rd123.")
            target_submit.click()

            sleep(15)

            alira_helper = AliraHelper(driver, page=0)
            excel_path = os.getcwd() + f"/resources/templates/seo/2022/12/KWR.xlsx"
            alira_helper.get_kwr(excel_path)

            """ CASINO ONLINE """
            alira_helper.get_sheet_url_reference(1, 5)
            references_1 = list(set(alira_helper.sheets[1].data))

            alira_helper.access_to_pages_tab()

            for reference in references_1:
                alira_helper.get_sheet_data(
                    1,
                    5,
                    [
                        f"https://www.casinoatlnaticcity.com",
                        f"https://www.casinoatlanticcity.com",
                    ])
                alira_helper.url = reference
                alira_helper.target_urls = [Url(index, s) for index, s in enumerate(alira_helper.sheets[1].data)]
                alira_helper.page = 1
                alira_helper.iterate_main_datatable()
                while alira_helper.page < alira_helper.table_page_total:
                    alira_helper.iterate_main_datatable()
            """ """

            """" APUESTAS DEPORTIVAS """
            alira_helper.get_sheet_url_reference(3, 3)
            references_2 = list(set(alira_helper.sheets[3].data))

            # alira_helper.access_to_pages_tab()

            for reference in references_2:
                alira_helper.get_sheet_data(
                    1,
                    5,
                    [
                        f"https://www.casinoatlnaticcity.com",
                        f"https://www.casinoatlanticcity.com",
                    ])
                alira_helper.url = reference
                alira_helper.target_urls = [Url(index, s) for index, s in enumerate(alira_helper.sheets[1].data)]
                alira_helper.page = 1
                alira_helper.iterate_main_datatable()
                while alira_helper.page < alira_helper.table_page_total:
                    alira_helper.iterate_main_datatable()

            alira.alira_helper = alira_helper
            driver.close()
            print('-------------------- finished -----------------------')

        except (UnicodeDecodeError, StopIteration) as e:

            print('error: ', e)

        return self.alira_repository.set_seo_parameters_per_page(alira)

    def get_layouts(self, alira: Alira):
        pass

    def set_page_url(self, alira: Alira):
        return alira