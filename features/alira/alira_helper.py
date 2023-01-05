from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait


class AliraHelper:

    def __init__(self, driver, url, page, title="", description="", seo="", reload=False):
        self.driver = driver
        self.url = url
        self.page = page
        self.title = title
        self.description = description
        self.seo = seo

    def access_to_pages_tab(self):
        if self.reload is True:
            self.driver.get(self.url)
            sleep(15)

        targets_menu = self.driver.find_elements(By.CSS_SELECTOR, ".has-submenu")
        print(f'------- munu list : {len(targets_menu)} ----------')

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

        table_target = Wait(self.driver, timeout=20).until(
            ec.visibility_of_element_located((By.ID, "allPagesEditor")))
        # table_target.click()
        table_input = table_target.find_elements(By.CSS_SELECTOR, "input")[2]
        table_input.send_keys("/casino-online")

        sleep(10)

        table_paginator = self.driver.find_element(By.CSS_SELECTOR, ".dataTables_paginate.paging_simple_numbers")
        table_paginator_options = table_paginator.find_elements(By.CSS_SELECTOR, "li")
        # table_paginator_next = driver.find_element(By.ID, "allPagesEditor_next")
        table_paginator_options_len = len(table_paginator_options)

        current_window = self.driver.current_window_handle

        if table_paginator_options_len > 2:
            table_page_total = int(table_paginator_options[table_paginator_options_len - 2].text.strip())
            print(f"-------- total pages: {table_page_total} ----------")
            for index in range(table_page_total):
                table_paginator_next = self.driver.find_element(By.ID, "allPagesEditor_next") \
                    .find_element(By.CSS_SELECTOR, "a")
                table_paginator_next.click()
                print(f"--------- index : {index} ----------")
                sleep(5)
                # action = ActionChains(driver)
                self.driver.execute_script(
                    f"var links = document.querySelectorAll('tbody a');"
                    "links.forEach(x => { x.setAttribute('target','_blank') });"
                    f""
                    F""
                )
                table_target = Wait(self.driver, timeout=20).until(
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

                        self.driver.switch_to.window(self.driver.window_handles[1])

                        self.driver.switch_to.window(current_window)
                        sleep(5)

                except (Exception, NoSuchElementException, StopIteration) as e:
                    print(f"Error : {e}")
        else:
            print("--------- no results -------------")
