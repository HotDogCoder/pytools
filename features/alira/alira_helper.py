from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait

from core.util.debug.trace_helper import TraceHelper
from core.util.excel.excel_helper import ExcelHelper
from core.util.excel.sheet import Sheet


class AliraHelper:

    def __init__(self, driver, url="", page=0, reload=False, layouts=[], target_urls=[], table_page_total=0):
        self.driver = driver
        self.url = url
        self.page = page
        self.reload = reload
        self.layouts = layouts
        self.target_urls = target_urls
        self.table_page_total = table_page_total
        self.sheets = []
        self.trace_helper = TraceHelper()

    def access_to_pages_tab(self):
        if self.reload is True:
            print("reload enabled")
            # self.driver.get(self.url)
            # sleep(15)

        targets_menu = self.driver.find_elements(By.CSS_SELECTOR, ".has-submenu")
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
                    print("cms link clicked")
                    raise StopIteration

        except (Exception, NoSuchElementException, StopIteration) as e:
            print(f"Error : {e}")

    def iterate_main_datatable(self):

        table_target = Wait(self.driver, timeout=30).until(
            ec.visibility_of_element_located((By.ID, "allPagesEditor")))
        # table_target.click()
        table_input = table_target.find_elements(By.CSS_SELECTOR, "input")[2]
        table_input.clear()
        table_input.send_keys(self.url)
        table_input.send_keys(Keys.RETURN)

        sleep(2)

        table_paginator = self.driver.find_element(By.CSS_SELECTOR, ".dataTables_paginate.paging_simple_numbers")
        table_paginator_options = table_paginator.find_elements(By.CSS_SELECTOR, "li")
        # table_paginator_next = driver.find_element(By.ID, "allPagesEditor_next")
        table_paginator_options_len = len(table_paginator_options) - 2

        current_window = self.driver.current_window_handle

        if table_paginator_options_len > 2:
            self.table_page_total = int(table_paginator_options[table_paginator_options_len].text.strip())

            print(f"-------- total pages: {self.table_page_total} ----------")
            try:
                # for index in range(self.table_page_total):
                if self.page > 1:
                    for thing in range(self.page - 1):
                        table_paginator_next_container = Wait(self.driver, timeout=20).until(
                            ec.visibility_of_element_located((By.ID, "allPagesEditor_next")))
                        table_paginator_next = table_paginator_next_container.find_element(By.CSS_SELECTOR, "a")
                        table_paginator_next.click()
                        sleep(2)

                print(f"--------- page : {self.page} ----------")

                table_target = Wait(self.driver, timeout=20).until(
                    ec.visibility_of_element_located((By.ID, "allPagesEditor")))

                sleep(2)

                table_target_tr_list = table_target.find_elements(By.CSS_SELECTOR, "tbody tr")

                try:
                    flag = False
                    for tr in table_target_tr_list:
                        tds = tr.find_elements(By.CSS_SELECTOR, "td")
                        target_urls = list(filter(lambda x: x.flag is True, self.target_urls))

                        if len(target_urls) == 0:
                            self.page = self.table_page_total
                            raise StopIteration

                        for target_url in target_urls:
                            target_url_str = target_url.url.strip()
                            td_str = ""
                            try:
                                td_str = tds[3].text
                                td_str = td_str.strip()
                            except Exception as e:
                                print(f"Error : {self.trace_helper.get_trace_str(e)}")
                            if target_url_str == td_str and target_url.flag is True:
                                print(f"there is a match with some url : {target_url.url}")
                                flag = True
                                print("searching for popup menu button")
                                new_tab_buttons = tr.find_elements(By.CSS_SELECTOR, "button")
                                new_tab_buttons[1].click()
                                sleep(1)
                                print("searching for link")
                                new_tab_links = tr.find_elements(By.CSS_SELECTOR, "a")
                                new_tab_links[1].click()
                                print("loading page link")
                                sleep(5)

                                target_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button")
                                for target_button in target_buttons:
                                    data_id = target_button.get_attribute("data-id")

                                    if data_id == "pageLayout":
                                        title = target_button.get_attribute("title")
                                        self.layouts.append(title)

                                cancel_page_button = self.driver.find_element(By.ID, "cancelPage")
                                cancel_page_button.click()
                                sleep(5)
                                target_url.flag = False
                                print(f"{target_url.url} was set it False")
                                print(target_urls)

                    if flag is False:
                        self.page = self.page + 1

                except (Exception, NoSuchElementException, StopIteration) as e:
                    print(f"Error : {self.trace_helper.get_trace_str(e)}")

                if self.page == self.table_page_total:
                    raise StopIteration

            except (NoSuchElementException, StopIteration) as e:
                print(f"Error : {self.trace_helper.get_trace_str(e)}")
        else:
            table_input.clear()
            self.page = self.table_page_total
            print("--------- no results -------------")

    def get_kwr(self, excel_path):

        sheets = [
            Sheet("Categorías", 0, [
                "N1 Actual",
                "Propuesta",
                "URL actual",
                "URL propuesta",
                "Acción SEO prioritarias",
                "KW 1",
                "SV 1",
                "KW 2",
                "SV 2",
                "KW 3",
                "SV 3",
                "KW 4",
                "SV 4",
                "KW 5",
                "SV 5",
                "KW 6",
                "SV 6",
                "KW 7",
                "SV 7",
                "KW 8",
                "SV 8",
                "KW 9",
                "SV 9",
                "H1",
                "Meta Title",
                "Len 1",
                "Meta Descripción",
                "Len 2",
                "Publicados metadatos",
                "Canonical"
            ]),
            Sheet("Casino online", 0, [
                "Subcategoría actual 1",
                "Subcategoría propuesta - N2",
                "Subcategoría actual 2",
                "Subcategoría propuesta - N3",
                "URL actual",
                "URL propuesta",
                "Acción SEO prioritarias",
                "KW 1",
                "SV 1",
                "KW 2",
                "SV 2",
                "KW 3",
                "SV 3",
                "KW 4",
                "SV 4",
                "KW 5",
                "SV 5",
                "KW 6",
                "SV 6",
                "KW 7",
                "SV 7",
                "KW 8",
                "SV 8",
                "KW 9",
                "SV 9",
                "H1",
                "Nuevo Meta Title",
                "Len 1",
                "Nueva  Meta Descripción",
                "Len 2",
                "Canonical",
            ]),
            Sheet("Footer casino online", 0, [
                "SECCION",
                "NOMBRE",
                "URL",
                "INDEX"
            ]),
            Sheet("Apuestas deportivas", 0, [
                "Subcategoría actual",
                "Subcategoría propuesta - N2",
                "URL actual",
                "URL propuesta",
                "Acción SEO prioritarias",
                "KW 1",
                "SV 1",
                "KW 2",
                "SV 2",
                "KW 3",
                "SV 3",
                "KW 4",
                "SV 4",
                "KW 5",
                "SV 5",
                "KW 6",
                "SV 6",
                "KW 7",
                "SV 7",
                "KW 8",
                "SV 8",
                "KW 9",
                "SV 9",
                "KW 10",
                "SV 10",
                "KW 11",
                "SV 11",
                "H1",
                "Nuevo Meta Title",
                "Len 1",
                "Nueva Meta Descripción",
                "Len 2",
                "Canonical"
            ]),
            Sheet("Footer apuestas deportivas", 0, [
                "SECCION",
                "NOMBRE",
                "URL",
                "INDEX"
            ])
        ]

        sheet_names = [sheets[i].name for i in range(len(sheets))]
        excel_helper = ExcelHelper(path=excel_path, sheet_name=sheet_names)
        for sheet in sheets:
            if len(sheet.columns) > 0:
                number_of_rows = excel_helper.df[sheet.name].shape[0]
                print(f"------ number_of_rows : {number_of_rows} -------")
                for time in range(number_of_rows):
                    row = excel_helper.get_row(sheet.name, time)
                    row_data = excel_helper.get_row_values(row, sheet.columns)
                    sheet.rows.append(row_data)
                self.sheets.append(sheet)

    def get_sheet_data(self, index, field_index, prefix=[]):
        for row in self.sheets[index].rows:
            if row[field_index]['value'] != "" and row[field_index]['value'] != "-":
                data_raw = row[field_index]['value']
                if len(prefix) > 0:
                    for p in prefix:
                        data_raw = data_raw.replace(p, "")
                self.sheets[index].data.append(data_raw)
        self.sheets[index].data = list(set(self.sheets[index].data))

    def get_sheet_url_reference(self, index, field_index, prefix=""):
        for row in self.sheets[index].rows:
            print(row)
            if row[field_index]['value'] != "" and row[field_index]['value'] != "-":
                data_raw = row[field_index]['value']
                if type(data_raw) == str:
                    if prefix != "":
                        data_raw = "/" + data_raw.replace(prefix, "")
                        data_raw = "/" + data_raw.split("/")[0]
                    else:
                        data_raw = data_raw.split("/")
                        data_raw = "/" + data_raw[3]
                    self.sheets[index].data.append(data_raw)
