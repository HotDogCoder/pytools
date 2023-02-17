import flet
import flet as ft
import pyautogui

from app.presentation.pages.alira_page import AliraPage
from app.presentation.pages.apuestas_deportivas.apuestas_deportivas_page import ApuestasDeportivasPage


def main(page: ft.page):
    alira_page = AliraPage()
    apuestas_deportivas_page = ApuestasDeportivasPage()

    screen_width, screen_height = pyautogui.size()

    page.window_width = 800
    page.window_height = 1000
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
            on_click=apuestas_deportivas_page.login_happy_ad
        ),
        width=screen_width,
        height=50
    )

    btn_test_login_happy_path_col = ft.Container(
        ft.FloatingActionButton
        (    text="LOGIN HAPPY PATH COL",
            icon=ft.icons.ARROW_RIGHT,
            on_click=apuestas_deportivas_page.login_happy_col()
        ),
        width=screen_width,
        height=50

    )


    btn_test_ad_promociones_1_0 = ft.Container(
        ft.FloatingActionButton(
            text="AD PROMOCIONES 1-0",
            icon=ft.icons.ARROW_RIGHT,
            on_click=apuestas_deportivas_page.ad_promociones_1_0
        ),
        width=screen_width,
        height=50
    )

    btn_test_col_promociones_1_0 = ft.Container(
        ft.FloatingActionButton(
            text="COL PROMOCIONES 1-0",
            icon=ft.icons.ARROW_RIGHT,
            on_click=apuestas_deportivas_page.col_promociones_1_0
        ),
        width=screen_width,
        height=50
    )

    btn_test_col_promocion_winner_de_winners = ft.Container(
        ft.FloatingActionButton(
            text="VISUALIZAR PROMOCION WINNER DE WINNERS",
            icon=ft.icons.ARROW_RIGHT,
            on_click=apuestas_deportivas_page.visualizar_promocion_winner_de_winners
        ),
        width=screen_width,
        height=50
    )

    btn_test_visualizar_depositos_col = ft.Container(
        ft.FloatingActionButton(
            text="VISUALIZAR DEPOSITOS COL",
            icon=ft.icons.ARROW_RIGHT,
            on_click=apuestas_deportivas_page.visualizar_depositos_col
        ),
        width=screen_width,
        height=50
    )

    btn_test_visualizar_depositos_ad = ft.Container(
        ft.FloatingActionButton(
            text="VISUALIZAR DEPOSITOS AD",
            icon=ft.icons.ARROW_RIGHT,
            on_click=apuestas_deportivas_page.visualizar_depositos_ad
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
                btn_test_login_happy_path_col,
                btn_test_ad_promociones_1_0,
                btn_test_col_promociones_1_0,
                btn_test_col_promocion_winner_de_winners,
                btn_test_visualizar_depositos_col,
                btn_test_visualizar_depositos_ad,
            ]
        )
    )


ft.app(target=main)
