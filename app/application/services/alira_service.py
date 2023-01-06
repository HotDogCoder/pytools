import math
import os
from time import sleep

import pytz
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait
from datetime import datetime, time
from app.application.services_interfaces.alira_service_interface import AliraServiceInterface
from app.domain.models.alira import Alira
from app.infrastructure.repositories.alira_repository import AliraRepository
from selenium.webdriver.common.action_chains import ActionChains

from core.domain.models.url import Url
from features.alira.alira_helper import AliraHelper
from features.excel.excel_helper import ExcelHelper
from features.excel.sheet import Sheet


class AliraService(AliraServiceInterface):

    def __init__(self):
        super().__init__()
        self.alira_repository = AliraRepository()

    def scroll_and_take_alira(self, alira: Alira, url, driver, target_iterations=None, zoom=None):

        tz = pytz.timezone('America/Bogota')
        directory_name = datetime.now(tz).strftime('%Y%m%d%H%M%S')
        driver.maximize_window()
        driver.get(url.url)

        targets = driver.find_elements(By.CSS_SELECTOR, ".react-grid-item")

        target = driver.find_element(By.CSS_SELECTOR, '.react-grid-layout')
        target_height = target.get_attribute('style')
        target_arr = target_height.split(' ')
        target_string = target_arr[1]
        target_string = target_string.strip()
        target_string = target_string.replace('}', '')
        target_string = target_string.replace("'", '')
        target_string = target_string.replace("px", '')
        target_string = target_string.replace(";", '')
        target_height_value = int(target_string)

        print(f'----------- number of chars : {len(targets)} ----------------')
        size = driver.get_window_size()
        target_height_clear = size.get('height') - 163 - 30 - 64 - 130

        if target_iterations is None:
            target_iterations = math.floor(target_height_value / target_height_clear)

        print(f"----------- screen height :{size.get('height')} ----------------")
        print(f"----------- scroll tag height : {target_string} ----------------")

        if zoom is not None:
            driver.execute_script(f"document.body.style.zoom='{zoom}%'")

        scroll_pause_time = 10

        sleep(scroll_pause_time)

        print(f"----------- scroll tag iterations : {target_iterations} ----------------")

        current_directory = os.getcwd()

        driver.save_alira(
            f"{current_directory}/storage/aliras/{alira.image_name_prefix}"
            f"{datetime.now().strftime('%y%m%d')}_0_{url.id}_{directory_name}.png")

        alira.image_list.append(
            f"{current_directory}/storage/aliras/{alira.image_name_prefix}"
            f"{datetime.now().strftime('%y%m%d')}_0_{url.id}_{directory_name}.png")

        sleep(5)

        for x in range(target_iterations):
            driver.execute_script(f"var scroll_targets = document.querySelectorAll('.scrollbar-view');"
                                  f"var scroll_target = scroll_targets[1];"
                                  f"scroll_target.scrollTo(0, {target_height_clear * (x + 1)});")

            sleep(5)

            driver.implicitly_wait(100)

            driver.save_alira(
                f"{current_directory}/storage/aliras/{alira.image_name_prefix}"
                f"{datetime.now().strftime('%y%m%d')}_{x + 1}_{url.id}.png")

            alira.image_list.append(
                f"{current_directory}/storage/aliras/{alira.image_name_prefix}"
                f"{datetime.now().strftime('%y%m%d')}_{x + 1}_{url.id}.png")

    def get_layouts_of_alira_page(self, alira: Alira):

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

            alira.alira_helper = alira_helper
            driver.close()
            print('-------------------- finished -----------------------')

        except (UnicodeDecodeError, StopIteration) as e:

            print('error: ', e)

        return self.alira_repository.get_layouts_of_alira_page(alira)
