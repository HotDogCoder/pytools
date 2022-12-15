from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait
import os
from datetime import datetime
from app.application.services_interfaces.screenshot_service_interface import ScreenshotServiceInterface
from app.domain.models.screenshot import Screenshot
from app.infrastructure.repositories.screenshot_repository import ScreenshotRepository


class ScreenshotService(ScreenshotServiceInterface):

    def __init__(self):
        super().__init__()
        self.screenshot_repository = ScreenshotRepository()

    def take_screenshot_servers_status_report(self, screenshot: Screenshot):

        try:
            driver = None
            url = screenshot.url
            match screenshot.driver:
                case 'Chrome':
                    driver = webdriver.Chrome()
                case 'Firefox':
                    driver = webdriver.Firefox()
                case 'Safari':
                    driver = webdriver.Safari()
                case 'Edge':
                    driver = webdriver.Edge()

            driver.maximize_window()
            driver.get(url)

            targets = driver.find_elements(By.CSS_SELECTOR, "header a")
            current_directory = os.getcwd()

            for target in targets:
                print(f'-------------------- {target.text} -----------------------')
                match target.text:
                    case 'INGRESAR':
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
                    case 'REGISTRATE':
                        # target.send_keys(Keys.ENTER)
                        # target.click()
                        break

            driver.close()

            # raise StopIteration

        except (UnicodeDecodeError, StopIteration) as e:

            print('error: ', e)

        return self.screenshot_repository.take_screenshot_servers_status_report(screenshot)

