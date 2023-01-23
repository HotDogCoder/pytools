# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSeleccionarID():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_seleccionarID(self):
    # Test name: Seleccionar ID 
    # Step # | name | target | value
    # 1 | open | https://atlanticcity.pre.tecnalis.com/casino-online | 
    self.driver.get("https://atlanticcity.pre.tecnalis.com/casino-online")
    # 2 | setWindowSize | 1536x824 | 
    self.driver.set_window_size(1536, 824)
    # 3 | click | css=#contentModalPlayerOculto img | 
    self.driver.find_element(By.CSS_SELECTOR, "#contentModalPlayerOculto img").click()
    # 4 | click | id=idAliraCampo | 
    self.driver.find_element(By.ID, "idAliraCampo").click()
    # 5 | type | id=idAliraCampo | 850
    self.driver.find_element(By.ID, "idAliraCampo").send_keys("850")
    # 6 | click | css=button:nth-child(4) | 
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()
    # 7 | mouseOver | css=.item-prev > button | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".item-prev > button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
  