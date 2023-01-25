from datetime import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from core.util.debug.trace_helper import TraceHelper


class CasinoHelper:
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

    def login_ad(self):
        # Test name: Login ingreso Happy
        # Step # | name | target | value
        # 1 | open | https://atlanticcity.pre.tecnalis.com/ |
        self.driver.get("https://atlantic:viQ[3UJ*Rk*Q1zC@atlanticcity.pre.tecnalis.com/")
        # 2 | setWindowSize | 1065x817 |
        self.driver.maximize_window()
        # 3 | click | css=.d-xl-block > .btn-casino |
        header = self.driver.find_element(BytesWarning.CSS_SELECTOR, "header")
        buttons = header.find_elements(By.CSS_SELECTOR, "a")
        for button in buttons:
            if button.text == "INGRESAR":
                button.click()
                time.sleep(5)
        # self.driver.find_element(By.CSS_SELECTOR, ".d-xl-block > .btn-casino").click()
        # 4 click to casino online
        wait = WebDriverWait(self.driver, 60)
        target_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cardDondeVamosSports > button")))
        target_button.click()
        # time.sleep(10)
        # 5 | type | id=username_aside | Testjordan01
        self.driver.find_element(By.ID, "username_aside").send_keys("Testjordan01")
        self.driver.find_element(By.ID, "password_aside").send_keys("Testjordan01")
        time.sleep(2)
        # 6| click | linkText=INGRESAR |
        self.driver.find_element(By.ID, "login_button_aside").click()
        time.sleep(10)

        self.driver.find_element(By.ID, "contentModalPlayerOculto").click()
        # 7 | type | id=idAliraCampo | 850
        self.driver.find_element(By.ID, "idAliraCampo").send_keys("850")
        # 8 | click | css=button:nth-child(4) |
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()
        # 9 | mouseOver | css=.item-prev > button |
        pass

    def login_ad(self):
        # Test name: Login ingreso Happy
        # Step # | name | target | value
        # 1 | open | https://atlanticcity.pre.tecnalis.com/ |
        self.driver.get("https://atlantic:viQ[3UJ*Rk*Q1zC@atlanticcity.pre.tecnalis.com/")
        # wait = WebDriverWait(self.driver, 10)
        # alert = wait.until(EC.alert_is_present())

        # Enter the username and password
        # alert.send_keys("atlantic")
        # alert.send_keys("\t")  # Tab to the password field
        # alert.send_keys("viQ[3UJ*Rk*Q1zC")

        # Accept the alert
        # alert.accept()
        # time.sleep(1)
        # 2 | setWindowSize | 1065x817 |
        self.driver.maximize_window()
        # 3 | click | css=.d-xl-block > .btn-casino |
        header = self.driver.find_element(By.CSS_SELECTOR, "header")
        buttons = header.find_elements(By.CSS_SELECTOR, "a")
        for button in buttons:
            if button.text == "INGRESAR":
                button.click()
                time.sleep(5)
        # self.driver.find_element(By.CSS_SELECTOR, ".d-xl-block > .btn-casino").click()
        # 4 click to casino online
        wait = WebDriverWait(self.driver, 60)
        target_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cardDondeVamosCasino > button")))
        target_button.click()
        # time.sleep(10)
        # 5 | type | id=username_aside | Testjordan01
        self.driver.find_element(By.ID, "username_aside").send_keys("Testjordan01")
        self.driver.find_element(By.ID, "password_aside").send_keys("Testjordan01")
        time.sleep(2)
        # 6| click | linkText=INGRESAR |
        self.driver.find_element(By.ID, "login_button_aside").click()
        time.sleep(10)

        self.driver.find_element(By.ID, "contentModalPlayerOculto").click()
        # 7 | type | id=idAliraCampo | 850
        self.driver.find_element(By.ID, "idAliraCampo").send_keys("850")
        # 8 | click | css=button:nth-child(4) |
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()
        # 9 | mouseOver | css=.item-prev > button |
        pass