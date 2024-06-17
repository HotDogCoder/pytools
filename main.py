import pytz
from datetime import datetime
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.chrome.service import Service
from abc import ABC, abstractmethod
from email import encoders
from email.mime.base import MIMEBase
from time import sleep
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class VisaModel:
    def __init__(
            self, 
            url, 
            image_name_prefix,
            driver, 
            task='schedule',
            email=None,
            password=None,
            is_schedule=False,
            intent_limit_input=None,
            chrome_driver_path=None,
            target_people="",
            delay_time=0,
            target_clients=[],
            client_index=0
        ):
        self.url = url
        self.image_name_prefix = image_name_prefix
        self.driver = driver
        self.image_list = []
        self.data_list = []
        self.task = task
        self.email = email
        self.password = password
        self.is_schedule = is_schedule
        self.intent_limit_input = intent_limit_input
        self.date = ""
        self.time = ""
        self.result = False
        self.chrome_driver_path = chrome_driver_path
        self.target_people = target_people
        self.delay_time = delay_time
        self.target_clients = target_clients
        self.client_index = client_index
        self.login_error_indexes = []
        self.done_indexes = []

class VisaHelper:
    def __init__(self, driver, visa_model=None):
        self.driver = driver
        self.visa_model = visa_model

    def login(self):
        self.driver.maximize_window()
        self.driver.get(self.visa_model.url)
        if (self.visa_model.client_index - 1) not in self.visa_model.done_indexes and  (self.visa_model.client_index - 1) not in self.visa_model.login_error_indexes:
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

            sleep(2)

            try:
                form = self.driver.find_element(By.ID, "sign_in_form")
                error = form.find_element(By.CSS_SELECTOR, ".error")
                if error.text != "":
                    print(f'Error: {"sign in error"}')
                    self.visa_model.login_error_indexes.append(self.visa_model.client_index - 1)
                    print(self.visa_model.login_error_indexes)

            except (NoSuchElementException) as e:
                sleep(7)
                pass

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
        try:
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
        except NoSuchElementException:
            current_date = datetime.now()
            body = f'Error al reprogramar la cita. Pagina en mantenimiento fecha: {current_date}.'
            to_targets = self.visa_model.target_people.split(",")
            for to in to_targets:
                print(f'target email: {to}')
                self.send_email(to_email=to, body=body, subject=f"Error al reprogramar la cita {self.visa_model.email}")
            

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
            if option_text == "":
                print("Target time not found.")
                pass
            else:
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
                to_targets = self.visa_model.target_people.split(",")
                
                if self.visa_model.is_schedule:
                    confirm_button.click()
                    body = f'Se re-agendo para el dia {self.visa_model.date} a las {self.visa_model.time}. Por favor, revisa la página de citas.'
                    for to in to_targets:
                        print(f'target email: {to}')
                        self.send_email(to_email=to, body=body, subject=f"Reagendamiento de cita {self.visa_model.email}")
                    sleep(3)
                else:
                    cancel_button = modal.find_element(By.CSS_SELECTOR, "a.button.secondary")
                    cancel_button.click()
                    body = f'Hay una nueva fecha de cita disponible el {self.visa_model.date} a las {self.visa_model.time}. Por favor, revisa la página de citas.'
                    for to in to_targets:
                        print(f'target email: {to}')
                        self.send_email(to_email=to, body=body)
                    # sleep(3)
                self.visa_model.result = True
                self.visa_model.done_indexes.append(self.visa_model.client_index - 1)

    def click_form(self, form_name):
        # Click on the reschedule button
        target_forms = self.driver.find_elements(By.CSS_SELECTOR, "a[role*='tab']")
        for form in target_forms:
            if form.text == form_name:
                form.click()
                return form
            
    def send_email(self, to_email="", body="", subject="'Nueva fecha de cita disponible'"):
        # logic to send a email
        # Create a message object
        msg = MIMEMultipart()
        msg['From'] = 'visasprograma@gmail.com'
        msg['To'] = to_email
        msg['Subject'] = subject

        # Add body to the email
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
        smtp_username = 'visasprograma@gmail.com'
        smtp_password = 'dmimuujxfjnkjxiy'

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
            
class VisaRepositoryInterface(ABC):
    def __init__(self):
        super().__init__()


    @abstractmethod
    def query(self, visa_model: VisaModel):
        return visa_model
    @abstractmethod
    def upload(self, visa_model: VisaModel):
        return visa_model
    @abstractmethod
    def post(self, visa_model: VisaModel):
        return visa_model
    @abstractmethod
    def get(self, visa_model: VisaModel):
        return visa_model
    @abstractmethod
    def put(self, visa_model: VisaModel):
        return visa_model
    @abstractmethod
    def delete(self, visa_model: VisaModel):
        return visa_model

class VisaRepository(VisaRepositoryInterface):
    def __init__(self):
        super().__init__()

    def query(self, visa_model: VisaModel):
        return visa_model
    def upload(self, visa_model: VisaModel):
        return visa_model
    def post(self, visa_model: VisaModel):
        return visa_model
    def get(self, visa_model: VisaModel):
        return visa_model
    def put(self, visa_model: VisaModel):
        return visa_model
    def delete(self, visa_model: VisaModel):
        return visa_model

class VisaServiceInterface(ABC):
    def __init__(self):
        super().__init__()


    @abstractmethod
    def query(self, visa_model: VisaModel):
        return visa_model
    @abstractmethod
    def upload(self, visa_model: VisaModel):
        return visa_model
    @abstractmethod
    def post(self, visa_model: VisaModel):
        return visa_model
    @abstractmethod
    def get(self, visa_model: VisaModel):
        return visa_model
    @abstractmethod
    def put(self, visa_model: VisaModel):
        return visa_model
    @abstractmethod
    def delete(self, visa_model: VisaModel):
        return visa_model

class VisaService(VisaServiceInterface):
    def __init__(self):
        super().__init__()
        self.visa_repository = VisaRepository()

    def query(self, visa_model: VisaModel):
        return self.visa_repository.query(visa_model)
    def upload(self, visa_model: VisaModel):
        return self.visa_repository.upload(visa_model)
    def post(self, visa_model: VisaModel):
        return self.visa_repository.post(visa_model)
    def get(self, visa_model: VisaModel):
        try:
            driver = None
            if visa_model.driver == 'Chrome':
                chrome_options = ChromeOptions()
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
                # chrome_options.add_argument('--headless')
                chrome_options.add_argument('--disable-gpu')
                chrome_service = Service(visa_model.chrome_driver_path)
                driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
            elif visa_model.driver == 'Firefox':
                driver = webdriver.Firefox()
            elif visa_model.driver == 'Safari':
                driver = webdriver.Safari()
            elif visa_model.driver == 'Edge':
                driver = webdriver.Edge()
            tz = pytz.timezone('America/Bogota')
            directory_name = datetime.now(tz).strftime('%Y%m%d%H%M%S')
            visa_helper = VisaHelper(driver, visa_model=visa_model)

            visa_helper.login()
            if (visa_model.client_index - 1) in visa_model.login_error_indexes:
                to_targets = visa_model.target_people.split(",")
                body = f'Error al iniciar sesión. Por favor, revisa las credenciales {visa_model.email} y {visa_model.password}.'
                for to in to_targets:
                    print(f'target email: {to}')
                    visa_helper.send_email(to_email=to, body=body, subject=f"Error al iniciar sesión {visa_model.email}")
            else:
                if visa_model.task == 'schedule':
                    visa_helper.schedule()
                elif visa_model.task == 'reschedule':
                    visa_helper.reschedule()
            driver.close()
        except (UnicodeDecodeError, StopIteration) as e:
            print('error: ', e)
        return self.visa_repository.get(visa_model)
    def put(self, visa_model: VisaModel):
        return self.visa_repository.put(visa_model)
    def delete(self, visa_model: VisaModel):
        return self.visa_repository.delete(visa_model)

class VisaController:
    def __init__(self):
        super().__init__()
        self.visa_service = VisaService()

    def query(self, visa_model: VisaModel):
        return self.visa_service.query(visa_model)
    def upload(self, visa_model: VisaModel):
        return self.visa_service.upload(visa_model)
    def post(self, visa_model: VisaModel):
        return self.visa_service.post(visa_model)
    def get(self, visa_model: VisaModel):
        print('VisaController.get')
        
        # while len(visa_model.target_clients) > (len(visa_model.login_error_indexes + visa_model.done_indexes)):
        #     if visa_model.client_index < len(visa_model.target_clients):
        #         visa_model.email = visa_model.target_clients[visa_model.client_index].cells[0].content.value
        #         visa_model.password = visa_model.target_clients[visa_model.client_index].cells[1].content.value
        #         print(visa_model.is_schedule)
        #         print(visa_model.intent_limit_input)
        #         print(visa_model.chrome_driver_path)
        #         print(visa_model.target_people)
        #         print(visa_model.delay_time)
        #         print(visa_model.target_clients)
        #         print(visa_model.client_index)
        #         print(visa_model.email)
        #         print(visa_model.password)
        #         visa_model.client_index += 1
        #         self.visa_service.get(visa_model)
        #         sleep(int(visa_model.delay_time))
            # self.visa_service.get(visa_model)
            # sleep(int(visa_model.delay_time))
        return self.visa_service.get(visa_model)
    def put(self, visa_model: VisaModel):
        return self.visa_service.put(visa_model)
    def delete(self, visa_model: VisaModel):
        return self.visa_service.delete(visa_model)

import pandas as pd

class Sheet:
    def __init__(self, name, row, columns=[]):
        self.name = name
        self.row = row
        self.columns = columns
        self.rows = []
        self.data = []

import pandas as pd

class ExcelHelper:
    def __init__(self, path="", sheet_name=None, header_present=True):
        self.path = path
        # Set header to None if no header is present in the Excel file
        header = 0 if header_present else None
        self.df = pd.read_excel(self.path, engine='openpyxl', sheet_name=sheet_name, header=header)

    def get_row_values(self, row_index):
        """Returns the values of a specific row given its index."""
        return self.df.iloc[row_index].values.tolist()

    def get_column_values(self, column_index):
        """Returns the values of a specific column given its index."""
        return self.df.iloc[:, column_index].tolist()

    def get_all_data(self):
        """Returns all the data from the dataframe as a list of lists."""
        return self.df.values.tolist()

import flet
import flet as ft
import pyautogui

def main(page: ft.page):

    screen_width, screen_height = pyautogui.size()

    page.window_width = 1000
    page.window_height = 1000
    text_field = ft.Container(
        ft.Text("AUTOMATIZADOR DE CITAS :", size=30, text_align=flet.TextAlign("center")),
        width=screen_width,
        height=50
    )

    excel_table = ft.DataTable(
        expand=True,
        border=ft.border.all(1, "black"),
        border_radius=5,
        vertical_lines=ft.border.BorderSide(1, "blue"),
        horizontal_lines=ft.border.BorderSide(1, "blue"),
        sort_column_index=0,
        sort_ascending=True,
        heading_row_height=30,
        data_row_color={"hovered": "0x30FF0000"},
        show_checkbox_column=True,
        divider_thickness=0,
        columns=[
            ft.DataColumn(
                ft.Text("Username"),
                on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
            ),
            ft.DataColumn(
                ft.Text("Password"),
                on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
            ),
            ft.DataColumn(
                ft.Text("Status"),
                on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
            ),
        ],
        rows=[],
    )

    excel_data_row = flet.Row([excel_table])

    def on_dialog_result(e: ft.FilePickerResultEvent):
        if e.files is None:
            return
        else:
            for file in e.files:
                print(file.name)
                print(file.path)
                excel_helper = ExcelHelper(path=file.path, sheet_name='Data', header_present=False)
                excel_data = excel_helper.get_all_data()
                excel_table.rows = []
                for row in excel_data:
                    excel_table.rows.append(
                        ft.DataRow(cells=[ft.DataCell(ft.Text(row[0], max_lines=2)), ft.DataCell(ft.Text(row[1])), ft.DataCell(ft.Text('CREATED'))]),
                    )
                page.update()

    excel_file = flet.FilePicker(on_result=on_dialog_result)
    page.overlay.append(excel_file)
    page.update()
    excel_file_button = ft.Container(
        ft.FloatingActionButton(
            text="Upload Excel File", 
            on_click=lambda _: excel_file.pick_files(allow_multiple=False),
            icon=ft.icons.CLOUD_UPLOAD
        ),
        height=50,
        expand=True
    )

    excel_file_row = flet.Row([excel_file_button])

    # Text field for email
    email_input = flet.TextField(label="Email", value="drivanguevara0627@yahoo.es")
    
    # Text field for password
    password_input = flet.TextField(label="Password", value="123456789")
    
    # Text field for limit of intents
    intent_limit_input = flet.TextField(label="Max Attempts", keyboard_type=ft.KeyboardType.NUMBER, value=0, expand=True)

    is_schedule = flet.Checkbox(label="Schedule", expand=True)

    chrome_driver_location = flet.TextField(label="Chrome driver path", value="C:/chromedriver", expand=True)

    delay_time = flet.TextField(label="Delay Time", keyboard_type=ft.KeyboardType.NUMBER, value=0, expand=True)

    def open_repo(e):
        page.launch_url('https://googlechromelabs.github.io/chrome-for-testing/')

    chrome_driver_link = ft.Container(
        ft.FloatingActionButton(
            text="",
            icon=ft.icons.DOWNLOAD,
            on_click=open_repo,
        ),
        height=50,
        expand=True
    )
    driver_row = flet.Row([chrome_driver_location, chrome_driver_link])

    target_people = flet.TextField(label="Target People", value="")

    dlg = ft.AlertDialog(
        title=ft.Text("Agrega personas en la lista de envios (target people)", size=20), on_dismiss=lambda e: print("suerte!")
    )
    
    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    second_row = flet.Row(
        [
            intent_limit_input,
            delay_time,
            is_schedule,
        ]
    )

    def schedule(e):
        driver = 'Chrome'
        image_name_prefix = 'alira_'

        if (target_people.value == ""):
            open_dlg(e)
            return

        visa_model = VisaModel(
            url="https://ais.usvisa-info.com/es-pe/niv/users/sign_in",
            image_name_prefix=image_name_prefix,
            driver=driver,
            visa_helper=None,
            task='schedule',
            email=email_input.value,
            password=password_input.value,
            is_schedule=is_schedule.value,
            intent_limit_input=intent_limit_input.value,
            
            chrome_driver_path=chrome_driver_location.value,
            target_people=target_people.value,
            delay_time=delay_time.value,
            target_clients=excel_table.rows
        )

        VC = VisaController()
        VC.get(visa_model=visa_model)

    def reschedule(e):
        driver = 'Chrome'
        image_name_prefix = 'alira_'

        if (target_people.value == ""):
            open_dlg(e)
            return

        visa_model = VisaModel(
            url="https://ais.usvisa-info.com/es-pe/niv/users/sign_in",
            image_name_prefix=image_name_prefix,
            driver=driver,
            task='reschedule',
            email=email_input.value,
            password=password_input.value,
            is_schedule=is_schedule.value,
            intent_limit_input=intent_limit_input.value,
            chrome_driver_path=chrome_driver_location.value,
            target_people=target_people.value,
            delay_time=delay_time.value,
            target_clients=excel_table.rows
        )

        VC = VisaController()
        while len(visa_model.target_clients) > (len(visa_model.login_error_indexes + visa_model.done_indexes)):
            if visa_model.client_index < len(visa_model.target_clients):
                visa_model.email = visa_model.target_clients[visa_model.client_index].cells[0].content.value
                visa_model.password = visa_model.target_clients[visa_model.client_index].cells[1].content.value
                print(visa_model.is_schedule)
                print(visa_model.intent_limit_input)
                print(visa_model.chrome_driver_path)
                print(visa_model.target_people)
                print(visa_model.delay_time)
                print(visa_model.target_clients)
                print(visa_model.client_index)
                print(visa_model.email)
                print(visa_model.password)
                visa_model.client_index += 1
                visa_model = VC.get(visa_model=visa_model)
                if visa_model.result:
                    excel_table.rows[visa_model.client_index] = ft.DataRow(cells=[ft.DataCell(ft.Text(visa_model.email, max_lines=2)), ft.DataCell(ft.Text(visa_model.password)), ft.DataCell(ft.Text('SUCCESS'))])
                if (visa_model.client_index - 1) in visa_model.login_error_indexes:
                    print(f'login error: {visa_model.client_index - 1}')
                    excel_table.rows[visa_model.client_index - 1] = ft.DataRow(cells=[ft.DataCell(ft.Text(visa_model.email, max_lines=2)), ft.DataCell(ft.Text(visa_model.password)), ft.DataCell(ft.Text('LOGIN ERROR'))])
                page.update()
                visa_model.result = False
                sleep(int(visa_model.delay_time))
            else:
                visa_model.client_index = 0
        

    btn_schedule = ft.Container(
        ft.FloatingActionButton(
            text="SCHEDULE",
            icon=ft.icons.CALENDAR_TODAY,
            on_click=schedule,
        ),
        height=50,
        expand=True,
        disabled=True
    )

    btn_reschedule = ft.Container(
        ft.FloatingActionButton(
            text="RESCHEDULE",
            icon=ft.icons.CALENDAR_TODAY,
            on_click=reschedule,
        ),
        height=50,
        expand=True
    )

    thrird_row = flet.Row(
        [
            btn_schedule,
            btn_reschedule,
        ]
    )

    page.add(
        ft.Column(
            [
                text_field,
                excel_file_row,
                excel_data_row,
                # email_input,
                # password_input,
                target_people,
                driver_row,
                second_row,
                thrird_row
            ]
        )
    )

    page.scroll = 'always'
    page.update()


ft.app(target=main)
