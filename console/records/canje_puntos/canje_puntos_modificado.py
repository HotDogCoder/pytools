import pytest
import time
import json
import unittest
from tabnanny import check
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC

class HelloWorld(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(18)
    
    #@pytest.mark.order(1)
    def test_inicioSesion(self):
        driver = self.driver
        driver.set_window_size(1552, 840)
        driver.get("https://atlantic:viQ%5B3UJ*Rk*Q1zC@atlanticcity.pre.tecnalis.com/")
        driver.find_element(By.LINK_TEXT, "INGRESAR").click()
        time.sleep(8)
        driver.find_element(By.CSS_SELECTOR, ".d-xl-block > .btn-casino").click()
        time.sleep(8)
        self.driver.find_element(By.ID, "username_aside").send_keys("PruebasFide3")
        #driver.find_element(By.CSS_SELECTOR, ".lista-botones > .a-button-primary").click()
        #driver.find_element(By.CSS_SELECTOR, ".lista-botones > .a-button-primary").click()
        driver.find_element(By.ID, "password_aside").send_keys("Fide2021")
        driver.find_element(By.ID, "ojoLogin").click()
        elements = driver.find_elements(By.CSS_SELECTOR, ".close-icon:nth-child(1)")
        assert len(elements) > 0
        elements = driver.find_elements(By.LINK_TEXT, "CREAR CUENTA")
        assert len(elements) > 0
        elements = driver.find_elements(By.LINK_TEXT, "¿OLVIDÓ SU CONTRASEÑA?")
        assert len(elements) > 0
        elements=driver.find_elements(By.ID, "recordar_pass")
        assert len(elements) > 0
        driver.find_element(By.ID, "login_button_aside").click()

    #@pytest.mark.order(2)
    def test_detalleproducto(self):
        driver = self.driver
        driver.get("https://atlantic:viQ%5B3UJ*Rk*Q1zC@atlanticcity.pre.tecnalis.com/casino-online")
        driver.set_window_size(1552, 840)
        driver.find_element(By.CSS_SELECTOR, ".lista-botones > .a-button-primary").click()
        time.sleep(8)
        self.driver.find_element(By.ID, "username_aside").send_keys("PruebasFide3")
        driver.find_element(By.ID, "password_aside").send_keys("Fide2021")
        time.sleep(8)
        driver.find_element(By.ID, "login_button_aside").click()
        time.sleep(8)
        driver.find_element(By.CSS_SELECTOR, ".material-icons-round").click()
        time.sleep(8)
        driver.find_element(By.CSS_SELECTOR, "li:nth-child(5) > #atlanticCityClubLeft-js").click()
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, "CANJE DE PUNTOS").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, ".direccion-ubicacion").click()
        time.sleep(5)
        driver.find_element(By.ID, "DireccionID_99954").click()
        #time.sleep(5)
        #elements = driver.find_elements(By.LINK_TEXT, "VOLVER")
        #assert len(elements) > 0
        driver.get("https://atlanticcity.pre.tecnalis.com/ver-detalle-de-producto-personalizado/?detalle-producto=126")

    def test_canjeproducto(self):
        driver = self.driver
        driver.get("https://atlantic:viQ%5B3UJ*Rk*Q1zC@atlanticcity.pre.tecnalis.com/casino-online")
        driver.set_window_size(1552, 840)
        driver.find_element(By.CSS_SELECTOR, ".lista-botones > .a-button-primary").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "username_aside").send_keys("PruebasFide3")
        driver.find_element(By.ID, "password_aside").send_keys("Fide2021")
        time.sleep(5)
        driver.find_element(By.ID, "login_button_aside").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, ".material-icons-round").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "li:nth-child(5) > #atlanticCityClubLeft-js").click()
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, "CANJE DE PUNTOS").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, ".direccion-ubicacion").click()
        time.sleep(5)
        driver.find_element(By.ID, "DireccionID_99954").click()
        time.sleep(5)
        driver.get("https://atlantic:viQ%5B3UJ*Rk*Q1zC@atlanticcity.pre.tecnalis.com/ver-detalle-de-producto-personalizado/?detalle-producto=112")
        time.sleep(8)
        driver.find_element(By.CSS_SELECTOR, ".button-plus").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, ".button-minus").click()
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,251)")
        time.sleep(4)
        element = driver.find_element(By.ID, "check3")
        print (element.is_selected())
         #!= True: element.click()
        time.sleep(5)
        elements = driver.find_elements(By.ID, "radiob4")
        assert len(elements) > 0
        #if elements.is_selected() != True: element.click()
        time.sleep(5)
        driver.find_element(By.ID, "btnagregar").click()
        time.sleep(8)
        driver.execute_script("window.scrollTo(0,201)")
        time.sleep(8)
        """"
        driver.find_element(By.LINK_TEXT, "IR AL CARRITO").click()
        time.sleep(8)   
        driver.get("https://atlanticcity.pre.tecnalis.com/carrito-de-compras-personalizado")
        time.sleep(8)
        driver.find_element(By.CSS_SELECTOR, ".btn-1-confirma").click()
        time.sleep(8)
        driver.find_element(By.CSS_SELECTOR, ".btn-2-confirma").click()
        time.sleep(8)
        driver.execute_script("window.scrollTo(0,0)")
        time.sleep(8)
        driver.find_element(By.LINK_TEXT, "IR AL HISTORIAL DE PEDIDOS").click()
        time.sleep(8)
        driver.get("https://atlanticcity.pre.tecnalis.com/historial-detalle-de-pedidos-personalizado")
        time.sleep(8)
        driver.find_element(By.CSS_SELECTOR, ".acc-toggler-titulo > .flex-grow-1").click()
        time.sleep(8)
        driver.find_element(By.CSS_SELECTOR, ".casino_online-12 > .n-pedido").click()
        time.sleep(8)
        driver.find_element(By.CSS_SELECTOR, ".p-2").click()
        time.sleep(8)
        driver.find_element(By.CSS_SELECTOR, ".p-2").click()
        time.sleep(8)
        driver.find_element(By.LINK_TEXT, "Completados").click()"""

    def teardown_method(self, method):
        self.driver.implicitly_wait(3)
        self.driver.close()
    
if __name__=="__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner (output = 'reportes',report_name  = 'hello-world-report'))
"""
    def test_canjeEfectivo(self):
        driver = self.driver
        driver.get("https://atlantic:viQ%5B3UJ*Rk*Q1zC@atlanticcity.pre.tecnalis.com/canjea-tus-puntos")
        driver.set_window_size(1552, 840)
        driver.find_element(By.LINK_TEXT, "Efectivo").click()
        driver.find_element(By.CSS_SELECTOR, ".disponible:nth-child(2) .checkmark").click()
        driver.find_element(By.CSS_SELECTOR, ".btn-add-efectivo").click()
        driver.execute_script("window.scrollTo(0,0)")
        driver.find_element(By.ID, "click-btn2-efectivo").click()
        driver.find_element(By.CSS_SELECTOR, ".btn-2-confirma").click()
        driver.find_element(By.CSS_SELECTOR, ".btn-2-confirma").click()
        driver.execute_script("window.scrollTo(0,0)")
        driver.find_element(By.LINK_TEXT, "IR AL HISTORIAL DE MIS PEDIDOS").click()
        driver.find_element(By.LINK_TEXT, "Completados").click()
        driver.find_element(By.CSS_SELECTOR, ".articulo-4446 > .acc-toggler-titulo > .flex-grow-1").click()
  
    def test_canjeEfectivoProducto(self):
        driver = self.driver
        driver.get("https://atlantic:viQ%5B3UJ*Rk*Q1zC@atlanticcity.pre.tecnalis.com/ver-detalle-de-producto-personalizado/?detalle-producto=112")
        driver.set_window_size(1552, 840)
        driver.find_element(By.CSS_SELECTOR, ".button-plus").click()
        driver.find_element(By.CSS_SELECTOR, ".button-minus").click()
        element = driver.find_element(By.ID, "check3")
        if element.is_selected() != True: element.click()
        element = driver.find_element(By.ID, "radiob4")
        if element.is_selected() != True: element.click()
        driver.find_element(By.ID, "btnagregar").click()
        driver.execute_script("window.scrollTo(0,201)")
        driver.find_element(By.LINK_TEXT, "SEGUIR CANJEANDO").click()
        driver.find_element(By.LINK_TEXT, "Efectivo").click()
        driver.find_element(By.CSS_SELECTOR, ".disponible:nth-child(2) > td:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, ".btn-add-efectivo").click()
        driver.execute_script("window.scrollTo(0,0)")
        driver.find_element(By.ID, "click-btn2-efectivo").click()
        driver.find_element(By.CSS_SELECTOR, ".button-plus").click()
        driver.find_element(By.CSS_SELECTOR, ".button-minus").click()
        driver.find_element(By.CSS_SELECTOR, ".btn-1-confirma").click()
        driver.find_element(By.CSS_SELECTOR, ".btn-2-confirma").click()
        driver.execute_script("window.scrollTo(0,0)")
        driver.find_element(By.LINK_TEXT, "IR AL HISTORIAL DE MIS PEDIDOS").click()
        driver.find_element(By.LINK_TEXT, "Completados").click()
    
    def test_cerrarSesin(self):
        driver = self.driver
        driver.get("https://atlantic:viQ%5B3UJ*Rk*Q1zC@atlanticcity.pre.tecnalis.com/casino-online")
        driver.set_window_size(1552, 840)
        driver.find_element(By.CSS_SELECTOR, ".a-button-secondary--dark:nth-child(3)").click()
        elements = driver.find_elements(By.CSS_SELECTOR, ".info-montos")
        assert len(elements) > 0
        elements = driver.find_elements(By.LINK_TEXT, "DEPOSITAR")
        assert len(elements) > 0
        elements = driver.find_elements(By.LINK_TEXT, "SALDOS  Y  RETIROS")
        assert len(elements) > 0
        elements = driver.find_elements(By.LINK_TEXT, "PERFIL")
        assert len(elements) > 0
        elements = driver.find_elements(By.LINK_TEXT, "CONTRASEÑA")
        assert len(elements) > 0
        elements = driver.find_elements(By.LINK_TEXT, "HISTORIAL")
        assert len(elements) > 0
        driver.find_element(By.LINK_TEXT, "CERRAR SESIÓN").click()
        elements = driver.find_elements(By.LINK_TEXT, "INGRESAR")
        assert len(elements) > 0"""

    
