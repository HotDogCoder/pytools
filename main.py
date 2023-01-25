import flet
import flet as ft
import pyautogui

from app.presentation.pages.alira_page import AliraPage
from app.presentation.pages.apuestas_deportivas.apuestas_deportivas_page import ApuestasDeportivasPage


def main(page: ft.page):
    alira_page = AliraPage()
    apuestas_deportivas_page = ApuestasDeportivasPage()

    screen_width, screen_height = pyautogui.size()

    page.window_width = 300
    page.window_height = 500
    text_field = ft.Container(
        ft.Text("QA TESTS :", size=30, text_align=flet.TextAlign("center")),
        width=screen_width,
        height=50
    )
    btn_test_alira_seo_setter = ft.Container(
        ft.FloatingActionButton(
            text="CAMBIAR CAMPOS DE SEO",
            icon=ft.icons.ARROW_RIGHT,
            on_click=alira_page.set_seo_parameters_per_page
        ),
        width=screen_width,
        height=50
    )

    btn_test_screenshot = ft.Container(
        ft.FloatingActionButton(
            text="MONITOREO",
            icon=ft.icons.ARROW_RIGHT,
            on_click=alira_page.take_screenshot_of_servers_status_1
        ),
        width=screen_width,
        height=50
    )

    btn_test_set_seo_redirection = ft.Container(
        ft.FloatingActionButton(
            text="REDIRECCIONES",
            icon=ft.icons.ARROW_RIGHT,
            on_click=alira_page.set_seo_redirection
        ),
        width=screen_width,
        height=50
    )

    btn_test_login_happy_path_ad = ft.Container(
        ft.FloatingActionButton(
            text="LOGIN HAPPY PATH AD",
            icon=ft.icons.ARROW_RIGHT,
            on_click=apuestas_deportivas_page.login_happy_path
        ),
        width=screen_width,
        height=50
    )

    btn_test_visualizar_torneos = ft.Container(
        ft.FloatingActionButton(
            text="VIZUALIZAR PROMOCIONES",
            icon=ft.icons.ARROW_RIGHT,
            on_click=apuestas_deportivas_page.visualizar_torneos
        ),
        width=screen_width,
        height=50
    )

    page.add(
        ft.Column(
            [
                text_field,
                btn_test_alira_seo_setter,
                btn_test_screenshot,
                btn_test_set_seo_redirection,
                btn_test_login_happy_path_ad,
                btn_test_visualizar_torneos
            ]
        )
    )


ft.app(target=main)
