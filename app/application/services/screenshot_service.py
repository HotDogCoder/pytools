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
from core.util.path.path_helper import PathHelper
from features.screenshot.screenshot_helper import ScreenshotHelper


class ScreenshotService(ScreenshotServiceInterface):

    def __init__(self):
        super().__init__()
        self.screenshot_repository = ScreenshotRepository()

    def take_screenshot_of_servers_status_1(self, screenshot: Screenshot):
        import datetime

        now = datetime.datetime.now()
        if now.hour >= 7 and now.minute >= 55:
            today = now.strftime("%Y-%m-%d")
        else:
            yesterday = (now - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            today = yesterday
        print(today)
        """"
        urls = [
            UrlModel(0, 'https://monitoreo.acity.com.pe/apps/platform/dashboard/3'),
            UrlModel(1, 'https://grafana.acity.com.pe/d/hT18KZz4z/monitoreo-url-internas?orgId=1&refresh=5s&from=now-1h&to=now'),
            UrlModel(2, 'https://grafana.acity.com.pe/d/LLSTg4zVz/estado-replica?orgId=1&refresh=5s&from=now-15m&to=now'),
            UrlModel(3, 'https://grafana.acity.com.pe/d/DjMVuiMVk/dashboard-casino-online?orgId=1&refresh=5s&from=now-15m&to=now'),
            UrlModel(4, 'https://grafana.acity.com.pe/d/-JFbnTn99/atlantic-express?orgId=1&refresh=5s&from=now-30m&to=now'),
            UrlModel(5, 'https://grafana.acity.com.pe/d/-JFbn66n4z/crmcloud?orgId=1&refresh=5s&from=now-30m&to=now'),
            UrlModel(6, 'https://grafana.acity.com.pe/d/-JFbnTn411/websol?orgId=1&refresh=5s&from=now-30m&to=now'),
            UrlModel(7, 'https://grafana.acity.com.pe/d/-JFbnT664z/genesys-y-crmcloud?orgId=1&refresh=5s&from=now-30m&to=now'),
            UrlModel(8, 'https://grafana.acity.com.pe/d/ac0OemdVk/total-competencias?orgId=1&refresh=5s&from=now-15m&to=now'),
            UrlModel(9, 'https://grafana.acity.com.pe/d/XYVkz7V4k/views-nzgp?orgId=1&refresh=5s'),
            UrlModel(10, 'https://grafana.acity.com.pe/d/k6RHcLo4k/atlantic-express-diario?orgId=1&refresh=5s&var-Fecha='+today+'&from=now-15m&to=now'),
        ]
        """
        report_types = self.screenshot_repository.get_all_report_types()


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

            path_helper = PathHelper()
            current_directory = path_helper.get_project_root_path()
            folder = f"{current_directory}/storage/screenshots"
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(e)

            for report_type in report_types:

                if report_type.id == 1:
                    print("1")
                    screenshot_helper.scroll_and_take_screenshot_monitoreo(screenshot, report_type, driver, zoom=50)

                elif report_type.id == 2:
                    print("2")
                    screenshot_helper.scroll_and_take_screenshot(screenshot, report_type, driver, zoom=50)

                elif report_type.id == 3:
                    print("3")
                    screenshot_helper.scroll_and_take_screenshot(screenshot, report_type, driver, target_iterations=0, zoom=45)

                elif report_type.id == 4:
                    print("4")
                    screenshot_helper.scroll_and_take_screenshot(screenshot, report_type, driver, target_iterations=0, zoom=50)


                elif report_type.id == 5:
                    print("5")
                    screenshot_helper.scroll_and_take_screenshot(screenshot, report_type, driver, zoom=50)

                elif report_type.id == 6:
                    print("6")
                    screenshot_helper.scroll_and_take_screenshot(screenshot, report_type, driver, zoom=50)

                elif report_type.id == 7:
                    print("7")
                    screenshot_helper.scroll_and_take_screenshot(screenshot, report_type, driver, zoom=50)

                elif report_type.id == 8:
                    print("8")
                    screenshot_helper.scroll_and_take_screenshot(screenshot, report_type, driver, zoom=50)

                elif report_type.id == 9:
                    print("9")
                    screenshot_helper.scroll_and_take_screenshot(screenshot, report_type, driver, target_iterations=0, zoom=30)

                elif report_type.id == 10:
                    print("10")
                    screenshot_helper.scroll_and_take_screenshot(screenshot, report_type, driver, zoom=50)

                elif report_type.id == 11:
                    print("11")
                    screenshot_helper.scroll_and_take_screenshot(screenshot, report_type, driver, target_iterations=0, zoom=39)

                else:
                    screenshot_helper.scroll_and_take_screenshot(screenshot, report_type, driver)
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

        except (UnicodeDecodeError, StopIteration) as e:import os
