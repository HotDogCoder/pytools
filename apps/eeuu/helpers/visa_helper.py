from email import encoders
from email.mime.base import MIMEBase
from time import sleep
from core.util.debug.trace_helper import TraceHelper
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class VisaHelper:
    def __init__(self, driver, visa_model=None):
        self.driver = driver
        self.visa_model = visa_model
        self.trace_helper = TraceHelper()

    def login(self):
        self.driver.maximize_window()
        self.driver.get(self.visa_model.url)
        form = self.driver.find_element(By.ID, "sign_in_form")
        actions = ActionChains(self.driver)
        actions.move_to_element(form)
        actions.perform()
        sleep(3)
        user_email = form.find_element(By.ID, "user_email")
        user_password = form.find_element(By.ID, "user_password")
        policy_confirmed = form.find_element(By.CSS_SELECTOR, ".icheck-label")
        target_submit = form.find_element(By.CSS_SELECTOR, "input[type='submit']")

        user_email.send_keys(self.visa_model.email)
        user_password.send_keys(self.visa_model.password)
        policy_confirmed.click()
        
        target_submit.click()

        sleep(7)

    def schedule(self):

        # # Select the first available date
        # target_date = self.driver.find_element(By.CSS_SELECTOR, ".ui-datepicker-calendar tbody tr:nth-child(2) td:nth-child(2)")
        # target_date.click()

        # # Select the first available time
        # target_time = self.driver.find_element(By.CSS_SELECTOR, ".time-slot-container .time-slot:nth-child(1)")
        # target_time.click()

        # # Click on the next button
        # target_next = self.driver.find_element(By.CSS_SELECTOR, ".btn-next")
        # target_next.click()

        # # Fill the form
        # target_name = self.driver.find_element(By.ID, "given_name")
        # target_name.send_keys("Dante")
        # target_surname = self.driver.find_element(By.ID, "surname")
        # target_surname.send_keys("Rojas")
        # target_email = self.driver.find_element(By.ID, "email")
        pass

    def reschedule(self):
        primary_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".button.primary")
        for button in primary_buttons:
            if button.text == "Continuar":
                button.click()
                break
        sleep(2)
        form = self.click_form("Reprogramar cita")
        div = form.find_element(By.XPATH, "./following-sibling::div")
        a = Wait(div, timeout=20).until(
                    ec.element_to_be_clickable((By.CSS_SELECTOR, "a")))
        # a = div.find_element(By.CSS_SELECTOR, "a")
        a.click()
        sleep(4)
        date = Wait(self.driver, timeout=50).until(
                    ec.element_to_be_clickable((By.ID, "appointments_consulate_appointment_date")))
        date.click()
        sleep(3)
        self.search_for_appointment()

        pass

    def search_for_appointment(self):
        
        max_attempts = int(self.visa_model.intent_limit_input)
        attempts = 0
        flag_found = False
        while not flag_found and attempts < max_attempts:
            datapicker = self.driver.find_element(By.ID, "ui-datepicker-div")
            try:
                target_date = datapicker.find_element(By.CSS_SELECTOR, "td[data-handler*='selectDay']")
                target_date.click()
                flag_found = True
                sleep(1)
            except NoSuchElementException:
                next_month = Wait(datapicker, timeout=20).until(
                    ec.element_to_be_clickable((By.CSS_SELECTOR, ".ui-datepicker-next")))
                next_month.click()
                sleep(1)
                attempts += 1
        if not flag_found:
            print("Target date not found after maximum attempts.")
            pass
        else:
            print("Target date found.")
            sleep(3)
            time_select = Wait(self.driver, timeout=20).until(
                    ec.element_to_be_clickable((By.ID, "appointments_consulate_appointment_time")))
            time_select.click()
            time_options = time_select.find_elements(By.CSS_SELECTOR, "option")
            option_text = ""
            for option in time_options:
                # trim the text
                option_text = option.text.strip()
                if option_text != "":
                    option.click()
                    break
            # press the down arrow key 1 time
            sleep(2)
            # self.visa_model.date = target_date.text
            self.visa_model.time = option_text
            """appointments_consulate_appointment_date"""
            input_date = self.driver.find_element(By.ID, "appointments_consulate_appointment_date")
            self.visa_model.date = input_date.get_attribute("value")
            # sleep(20)

            sleep(2)
            """<input type="submit" name="commit" value="Reprogramar" id="appointments_submit" disabled="disabled" data-confirm="{&quot;title&quot;:&quot;¿Desea reprogramar esta cita?&quot;,&quot;ok&quot;:&quot;Confirmar&quot;,&quot;cancel&quot;:&quot;Cancelar&quot;}" data-disable-with="Por favor, espere." class="button primary">""" 
            submit_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
            submit_button.click()
    
            """
            <div data-reveal="nmkq7l-reveal" class="reveal " role="dialog" aria-hidden="false" tabindex="-1" style="display: block; top: 163px;">
            <h2 data-confirm-title="" class="h3 text-center alert-icon">¿Desea reprogramar esta cita?</h2>
            <p data-confirm-body="" class=""></p>
            <div data-confirm-footer="" class="text-center">
                <a data-confirm-cancel="" class="button secondary">Cancelar</a>
            <a class="button alert">Confirmar</a></div>
            <a aria-label="Close modal" class="close-button" data-close="">
            <span aria-hidden="true" class="fas fa-times"></span>
            </a>
            </div>
            """

            modal = Wait(self.driver, timeout=20).until(
                    ec.element_to_be_clickable((By.CSS_SELECTOR, "div[data-reveal]")))
            confirm_button = modal.find_element(By.CSS_SELECTOR, "a.button.alert")
            self.send_email()
            if self.visa_model.is_schedule:
                confirm_button.click()
                sleep(3)
            else:
                cancel_button = modal.find_element(By.CSS_SELECTOR, "a.button.secondary")
                cancel_button.click()
                # sleep(3)
            self.visa_model.result = True

    def click_form(self, form_name):
        # Click on the reschedule button
        target_forms = self.driver.find_elements(By.CSS_SELECTOR, "a[role*='tab']")
        for form in target_forms:
            if form.text == form_name:
                form.click()
                return form
            
    def send_email(self):
        # logic to send a email
        # Create a message object
        msg = MIMEMultipart()
        msg['From'] = 'jhospinal@acidjelly.com'
        msg['To'] = 'jorgehospinalflores@gmail.com'
        msg['Subject'] = 'Nueva fecha de cita disponible'

        # Add body to the email
        body = f'Hay una nueva fecha de cita disponible el {self.visa_model.date} {self.visa_model.time}. Por favor, revisa la página de citas.'
        msg.attach(MIMEText(body, 'plain'))

        # Attach a file to the email (optional)
        # filename = 'attachment.txt'
        # attachment = open(filename, 'rb')
        # part = MIMEBase('application', 'octet-stream')
        # part.set_payload((attachment).read())
        # encoders.encode_base64(part)
        # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        # msg.attach(part)

        # Send the email
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'jhospinal@acidjelly.com'
        smtp_password = 'keeixhzqccfuibtm'

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)