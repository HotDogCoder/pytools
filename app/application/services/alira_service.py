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

            match alira.driver:
                case 'Chrome':
                    driver = webdriver.Chrome()
                case 'Firefox':
                    driver = webdriver.Firefox()
                case 'Safari':
                    driver = webdriver.Safari()
                case 'Edge':
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

            targets_menu = driver.find_elements(By.CSS_SELECTOR, ".has-submenu")
            print(f'------- menu list : {len(targets_menu)} ----------')

            target_menu = None

            try:
                for target in targets_menu:
                    targets_menu_span = target.find_element(By.CSS_SELECTOR, ".text-uppercase")
                    targets_menu_a = target.find_element(By.CSS_SELECTOR, "a")
                    text = targets_menu_span.text.strip()
                    print(f'-------------------- text : {text} -----------------------')

                    if text == "SITIO WEB":
                        if target_menu is None:
                            target_menu = target
                        targets_menu_a.click()
                        sleep(5)
                        print("uwu")
                        raise StopIteration

            except (Exception, NoSuchElementException, StopIteration) as e:
                    print(f"Error : {e}")

            target_menu_submenu_items = target_menu.find_elements(By.CSS_SELECTOR, "li")
            print(f'---------- sub menu items : {len(target_menu_submenu_items)} ------------')
            # target_menu_submenu_cms = None

            try:
                for submenu_target in target_menu_submenu_items:
                    # target_menu_submenu_cms = target
                    targets_menu_a = submenu_target.find_element(By.CSS_SELECTOR, "a")
                    text = targets_menu_a.text.strip()
                    print(f'-------------------- text : {text} -----------------------')

                    if text == "CMS":
                        targets_menu_a.click()
                        sleep(15)
                        print("uwu")
                        raise StopIteration

            except (Exception, NoSuchElementException, StopIteration) as e:
                print(f"Error : {e}")

            table_target = Wait(driver, timeout=20).until(
                ec.visibility_of_element_located((By.ID, "allPagesEditor")))
            # table_target.click()
            table_input = table_target.find_elements(By.CSS_SELECTOR, "input")[2]
            table_input.send_keys("/casino-online")

            sleep(10)

            table_paginator = driver.find_element(By.CSS_SELECTOR, ".dataTables_paginate.paging_simple_numbers")
            table_paginator_options = table_paginator.find_elements(By.CSS_SELECTOR, "li")
            # table_paginator_next = driver.find_element(By.ID, "allPagesEditor_next")
            table_paginator_options_len = len(table_paginator_options)

            current_window = driver.current_window_handle

            if table_paginator_options_len > 2:
                table_page_total = int(table_paginator_options[table_paginator_options_len - 2].text.strip())
                print(f"-------- total pages: {table_page_total} ----------")
                for index in range(table_page_total):
                    table_paginator_next = driver.find_element(By.ID, "allPagesEditor_next")\
                        .find_element(By.CSS_SELECTOR, "a")
                    table_paginator_next.click()
                    print(f"--------- index : {index} ----------")
                    sleep(5)
                    # action = ActionChains(driver)
                    driver.execute_script(
                        f"var links = document.querySelectorAll('tbody a');"
                        "links.forEach(x => { x.setAttribute('target','_blank') });"
                        f""
                        F""
                    )
                    table_target = Wait(driver, timeout=20).until(
                        ec.visibility_of_element_located((By.ID, "allPagesEditor")))

                    table_target_tr_list = table_target.find_elements(By.CSS_SELECTOR, "tbody tr")

                    try:
                        for tr in table_target_tr_list:
                            new_tab_buttons = tr.find_elements(By.CSS_SELECTOR, "button")
                            # print(f"-----------  TR : {new_tab_link} ------------")
                            # action.key_down(Keys.CONTROL).click(new_tab_link).key_up(Keys.CONTROL).perform()
                            new_tab_buttons[1].click()
                            new_tab_links = tr.find_elements(By.CSS_SELECTOR, "a")
                            # print(f"-----------  TR : {new_tab_link} ------------")
                            # action.key_down(Keys.CONTROL).click(new_tab_link).key_up(Keys.CONTROL).perform()
                            new_tab_links[1].click()
                            sleep(5)

                            driver.switch_to.window(driver.window_handles[1])

                            driver.switch_to.window(current_window)
                            sleep(5)

                    except (Exception, NoSuchElementException, StopIteration) as e:
                        print(f"Error : {e}")
            else:
                print("--------- no results -------------")

            driver.close()
            print('-------------------- finished -----------------------')

        except (UnicodeDecodeError, StopIteration) as e:

            print('error: ', e)

        return self.alira_repository.get_layouts_of_alira_page(alira)
