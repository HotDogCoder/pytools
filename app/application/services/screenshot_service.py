import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait
from datetime import datetime
from app.application.services_interfaces.screenshot_service_interface import ScreenshotServiceInterface
from app.domain.models.screenshot import Screenshot
from core.domain.models.url import Url as ReportType
from app.infrastructure.repositories.screenshot_repository import ScreenshotRepository
from features.screenshot.screenshot_helper import ScreenshotHelper


class ScreenshotService(ScreenshotServiceInterface):

    def __init__(self):
        super().__init__()
        self.screenshot_repository = ScreenshotRepository()

    def take_screenshot_of_servers_status_1(self, screenshot: Screenshot):

        report_types = self.screenshot_repository.get_all_report_types()

        return self.screenshot_repository.take_screenshot_of_servers_status_1(screenshot)

    """
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

            screenshot_helper = ScreenshotHelper()

            for report_type in report_types:

                if report_type.id == 1:
                    screenshot_helper.scroll_and_take_screenshot_monitoreo(screenshot, report_type, driver, zoom=50)

                elif report_type.id == 2:
                    print("1")
                    screenshot_helper.scroll_and_take_screenshot(screenshot, report_type, driver, zoom=50)

                elif report_type.id == 3:
                    print("2")
                    screenshot_helper.scroll_and_take_screenshot(screenshot, report_type, driver, target_iterations=0, zoom=30)

                elif report_type.id == 4:
                    print("3")
                    screenshot_helper.scroll_and_take_screenshot(screenshot, report_type, driver, target_iterations=0, zoom=35)

                elif report_type.id == 5:
                    print("4")
                    screenshot_helper.scroll_and_take_screenshot(screenshot, report_type, driver, zoom=40)

                elif report_type.id == 6:
                    print("5")
                    screenshot_helper.scroll_and_take_screenshot(screenshot, report_type, driver, target_iterations=0, zoom=20)

                elif report_type.id == 7:
                    print("6")
                    screenshot_helper.scroll_and_take_screenshot(screenshot, report_type, driver, zoom=38)

                else:
                    screenshot_helper.scroll_and_take_screenshot(screenshot, report_type, driver)
                    pass

            driver.close()
            print('-------------------- finished -----------------------')

        except (UnicodeDecodeError, StopIteration) as e:

            print('error: ', e)
    """

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
