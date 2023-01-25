import flet
import flet as ft
import pyautogui

from app.presentation.pages.alira_page import AliraPage


def main(page: ft.page):
    alira_page = AliraPage()

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

    page.add(
        ft.Column(
            [
                text_field,
                btn_test_alira_seo_setter,
                btn_test_screenshot,
                btn_test_set_seo_redirection
            ]
        )
    )


ft.app(target=main)
