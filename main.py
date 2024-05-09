from apps.eeuu.domain.models.visa_model import VisaModel
from apps.eeuu.presentation.controllers.visa_controller import VisaController
from apps.eeuu.presentation.pages.visa_page import VisaPage
import flet
import flet as ft
import pyautogui

def main(page: ft.page):
    visa_page = VisaPage()

    screen_width, screen_height = pyautogui.size()

    page.window_width = 500
    page.window_height = 500
    text_field = ft.Container(
        ft.Text("AUTOMATIZADOR DE CITAS :", size=30, text_align=flet.TextAlign("center")),
        width=screen_width,
        height=50
    )

    # Text field for email
    email_input = flet.TextField(label="Email", value="drivanguevara0627@yahoo.es")
    
    # Text field for password
    password_input = flet.TextField(label="Password", value="123456789")
    
    # Text field for limit of intents
    intent_limit_input = flet.TextField(label="Max Attempts", keyboard_type=ft.KeyboardType.NUMBER, value=15)

    is_schedule = flet.Checkbox(label="Schedule")

    second_row = flet.Row(
        [
            intent_limit_input,
            is_schedule,
        ]
    )

    def schedule(e):
        driver = 'Chrome'
        image_name_prefix = 'alira_'

        visa_model = VisaModel(
            url="https://ais.usvisa-info.com/es-pe/niv/users/sign_in",
            image_name_prefix=image_name_prefix,
            driver=driver,
            visa_helper=None,
            task='schedule',
            email=email_input.value,
            password=password_input.value,
            is_schedule=is_schedule.value,
            intent_limit_input=intent_limit_input.value
        )

        VC = VisaController()
        VC.get(visa_model=visa_model)

    def reschedule(e):
        driver = 'Chrome'
        image_name_prefix = 'alira_'

        visa_model = VisaModel(
            url="https://ais.usvisa-info.com/es-pe/niv/users/sign_in",
            image_name_prefix=image_name_prefix,
            driver=driver,
            task='reschedule',
            email=email_input.value,
            password=password_input.value,
            is_schedule=is_schedule.value,
            intent_limit_input=intent_limit_input.value
        )

        VC = VisaController()
        VC.get(visa_model=visa_model)

    btn_schedule = ft.Container(
        ft.FloatingActionButton(
            text="SCHEDULE",
            icon=ft.icons.CALENDAR_TODAY,
            on_click=schedule,
        ),
        height=50,
        expand=True
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
                email_input,
                password_input,
                second_row,
                thrird_row
            ]
        )
    )


ft.app(target=main)
