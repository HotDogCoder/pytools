import math
import os
from time import sleep

import pytz
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait
from datetime import datetime
from app.application.services_interfaces.screenshot_service_interface import ScreenshotServiceInterface
from app.domain.models.screenshot import Screenshot
from core.domain.models.url import Url as UrlModel
from app.infrastructure.repositories.screenshot_repository import ScreenshotRepository


class ScreenshotService(ScreenshotServiceInterface):

    def __init__(self):
        super().__init__()
        self.screenshot_repository = ScreenshotRepository()

    @staticmethod
    def scroll_and_take_screenshot(screenshot: Screenshot, url, driver, target_iterations=None, zoom=None):

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

        scrollHeight = driver.execute_script(
            f"var scroll_targets = document.querySelectorAll('.scrollbar-view');"
            f"var scroll_target = scroll_targets[1];"

        )
        if zoom is not None:
            """
            // Get the height of the document
            var scrollHeight = document.body.scrollHeight;

            // Get the height of the viewable area
            var clientHeight = document.documentElement.clientHeight;

            // Get the current scroll position
            var scrollTop = window.pageYOffset;

            // Calculate the maximum number of scrolls
            var maxScrolls = Math.ceil( (scrollHeight - clientHeight) / scrollTop);
            """
            driver.execute_script(f"document.body.style.zoom='{zoom}%'")

        scroll_pause_time = 10

        sleep(scroll_pause_time)

        print(f"----------- scroll tag iterations : {target_iterations} ----------------")

        current_directory = os.getcwd()

        driver.save_screenshot(
            f"{current_directory}/storage/screenshots/{screenshot.image_name_prefix}"
            f"{datetime.now().strftime('%y%m%d')}_0_{url.id}_{directory_name}.png")

        screenshot.image_list.append(
            f"{current_directory}/storage/screenshots/{screenshot.image_name_prefix}"
            f"{datetime.now().strftime('%y%m%d')}_0_{url.id}_{directory_name}.png")

        sleep(5)

        for x in range(target_iterations):
            driver.execute_script(f"var scroll_targets = document.querySelectorAll('.scrollbar-view');"
                                  f"var scroll_target = scroll_targets[1];"
                                  f"scroll_target.scrollTo(0, {target_height_clear * (x + 1)});")

            sleep(5)

            driver.implicitly_wait(100)

            driver.save_screenshot(
                f"{current_directory}/storage/screenshots/{screenshot.image_name_prefix}"
                f"{datetime.now().strftime('%y%m%d')}_{x + 1}_{url.id}.png")

            screenshot.image_list.append(
                f"{current_directory}/storage/screenshots/{screenshot.image_name_prefix}"
                f"{datetime.now().strftime('%y%m%d')}_{x + 1}_{url.id}.png")

    @staticmethod
    def scroll_and_take_screenshot_monitoreo(screenshot: Screenshot, url, driver):

        tz = pytz.timezone('America/Bogota')
        directory_name = datetime.now(tz).strftime('%Y%m%d%H%M%S')

        driver.maximize_window()
        driver.get(url.url)

        scroll_pause_time = 10

        target = driver.find_element(By.CSS_SELECTOR, 'html')

        size = driver.get_window_size()
        target_height_clear = size.get('height') - 163 - 30 - 64 - 130
        target_height_value = driver.execute_script("return document.querySelector('html').scrollHeight")
        target_iterations = math.floor(target_height_value / target_height_clear)

        print(f"----------- screen height :{size.get('height')} ----------------")
        print(f"----------- scroll tag height : {target_height_value} ----------------")

        sleep(scroll_pause_time)
        print(f"----------- scroll tag iterations : {target_iterations} ----------------")

        current_directory = os.getcwd()

        driver.save_screenshot(
            f"{current_directory}/storage/screenshots/{screenshot.image_name_prefix}"
            f"{datetime.now().strftime('%y%m%d')}_0_{url.id}_{directory_name}.png")

        screenshot.image_list.append(
            f"{current_directory}/storage/screenshots/{screenshot.image_name_prefix}"
            f"{datetime.now().strftime('%y%m%d')}_0_{url.id}_{directory_name}.png")

    def take_screenshot_of_servers_status_1(self, screenshot: Screenshot):

        urls = [
            UrlModel(0, 'https://monitoreo.acity.com.pe/apps/platform/dashboard/3'),
            UrlModel(1, 'https://grafana.acity.com.pe/d/hT18KZz4z/monitoreo-url-internas?orgId=1&refresh=5s'),
            UrlModel(2, 'https://grafana.acity.com.pe/d/LLSTg4zVz/estado-replica?orgId=1&refresh=5s'),
            UrlModel(3, 'https://grafana.acity.com.pe/d/DjMVuiMVk/dashboard-casino-online?orgId=1&refresh=5s'),
            UrlModel(4, 'https://grafana.acity.com.pe/d/-JFbnTn4z/estado-aplicaciones-web?orgId=1&refresh=5s'),
            UrlModel(5, 'https://grafana.acity.com.pe/d/ac0OemdVk/total-competencias?orgId=1&refresh=5s'),
            UrlModel(6, 'https://grafana.acity.com.pe/d/XYVkz7V4k/views-nzgp?orgId=1&refresh=5s')
        ]

        try:
            driver = None
            # url = screenshot.url
            if screenshot.driver == 'Chrome':
                driver = webdriver.Chrome()
            elif screenshot.driver == 'Firefox':
                driver = webdriver.Firefox()
            elif screenshot.driver == 'Safari':
                driver = webdriver.Safari()
            elif screenshot.driver == 'Edge':
                driver = webdriver.Edge()

            for url in urls:

                if url.id == 0:
                    self.scroll_and_take_screenshot_monitoreo(screenshot, url, driver)

                elif url.id == 1:
                    self.scroll_and_take_screenshot(screenshot, url, driver)

                elif url.id == 2:
                    self.scroll_and_take_screenshot(screenshot, url, driver, target_iterations=0, zoom=50)

                elif url.id == 3:
                    self.scroll_and_take_screenshot(screenshot, url, driver, target_iterations=0, zoom=70)

                elif url.id == 4:
                    self.scroll_and_take_screenshot(screenshot, url, driver, zoom=80)

                elif url.id == 5:
                    self.scroll_and_take_screenshot(screenshot, url, driver, target_iterations=0, zoom=40)

                elif url.id == 6:
                    self.scroll_and_take_screenshot(screenshot, url, driver, zoom=75)

                else:
                    self.scroll_and_take_screenshot(screenshot, url, driver)
                    pass

            driver.close()
            print('-------------------- finished -----------------------')

        except (UnicodeDecodeError, StopIteration) as e:

            print('error: ', e)

        return self.screenshot_repository.take_screenshot_of_servers_status_1(screenshot)

    def test_atlantic_city_casino_and_sports(self, screenshot: Screenshot):

        try:
            driver = None
            url = screenshot.url
            if screenshot.driver == 'Chrome':
                driver = webdriver.Chrome()
            elif screenshot.driver == 'Firefox':
                driver = webdriver.Firefox()
            elif screenshot.driver == 'Safari':
                driver = webdriver.Safari()
            elif screenshot.driver == 'Edge':
                driver = webdriver.Edge()

            driver.maximize_window()
            driver.get(url)

            targets = driver.find_elements(By.CSS_SELECTOR, "header a")
            current_directory = os.getcwd()

            for target in targets:
                print(f'-------------------- {target.text} -----------------------')

                if target.text == 'INGRESAR':
                        target.click()
                        new_target = Wait(driver, timeout=10).until(
                            ec.visibility_of_element_located((By.CSS_SELECTOR, ".btn-sports")))
                        new_target.click()
                        driver.implicitly_wait(10)
                        driver.save_screenshot(
                            f"{current_directory}/storage/screenshots/{screenshot.image_name_prefix}"
                            f"{datetime.now().strftime('%y%m%d')}.png")

                        screenshot.image_list.append(
                            f"{current_directory}/storage/screenshots/{screenshot.image_name_prefix}"
                            f"{datetime.now().strftime('%y%m%d')}.png")

                        break
                elif target.text == 'REGISTRATE':
                        # target.send_keys(Keys.ENTER)
                        # target.click()
                        break

            driver.close()

            # raise StopIteration

        except (UnicodeDecodeError, StopIteration) as e:

            print('error: ', e)

        return self.screenshot_repository.test_atlantic_city_casino_and_sports(screenshot)
