from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from core.util.debug.trace_helper import TraceHelper


class ApuestasDeportivasHelper:
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

        self.driver.get(self.url)
        self.driver.maximize_window()
        """INGRESA A EL BOTON INGRESAR"""
        header = self.driver.find_element(By.CSS_SELECTOR, "header")
        buttons = header.find_elements(By.CSS_SELECTOR, "a")
        for button in buttons:
            if button.text == "INGRESAR":
                button.click()
                sleep(5)
        """A DONDE VAMOS  IR A SPORTS"""
        wait = WebDriverWait(self.driver, 60)
        target_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cardDondeVamosSports > button")))
        target_button.click()
        # time.sleep(10)
        # 5 | type | id=username_aside | Testjordan01

    def cerrar_sesión_ad(self):
        """INGRESA AL MENÚ"""
        header = self.driver.find_element(By.CSS_SELECTOR, "header.o-header")
        micuenta = header.find_elements(By.CSS_SELECTOR, "a")
        for button in micuenta:
            if button.text == "person":
                button.click()
                sleep(5)
        """CLICK EN CERRAR SESIÓN"""
        aside = self.driver.find_element(By.CSS_SELECTOR, "aside.o-aside.fixed-right")
        cerrarsesión = aside.find_elements(By.CSS_SELECTOR, "a")
        for buttond in cerrarsesión:
            if buttond.text == "CERRAR SESIÓN":
                buttond.click()
                sleep(6)

