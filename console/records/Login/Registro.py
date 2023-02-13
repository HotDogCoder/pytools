import time

from selenium.webdriver.common.by import By


class Registro():



    def registro_paciente(self):

        self.driver.get("https://atlantic:viQ[3UJ*Rk*Q1zC@atlanticcity.pre.tecnalis.com/")

        nombres = self.driver.find_element(By.CSS.SELECTOR,"ng-dirty").send_keys("Jordan").click

        time.sleep(10)









registro_paciente = Registro