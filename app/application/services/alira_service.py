import os
from time import sleep

import pytz
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from app.application.services_interfaces.alira_service_interface import AliraServiceInterface
from app.domain.models.alira import Alira
from app.infrastructure.repositories.alira_repository import AliraRepository

from core.domain.models.url import Url
from core.util.debug.trace_helper import TraceHelper
from features.alira.alira_helper import AliraHelper


class AliraService(AliraServiceInterface):

    def __init__(self):
        super().__init__()
        self.alira_repository = AliraRepository()

    def set_seo_parameters_per_page(self, alira: Alira):

        try:
            driver = None

            if alira.driver == 'Chrome':
                driver = webdriver.Chrome()
            elif alira.driver == 'Firefox':
                driver = webdriver.Firefox()
            elif alira.driver == 'Safari':
                driver = webdriver.Safari()
            elif alira.driver == 'Edge':
                driver = webdriver.Edge()

            tz = pytz.timezone('America/Bogota')
            directory_name = datetime.now(tz).strftime('%Y%m%d%H%M%S')

            alira.alira_helper = AliraHelper(driver, page=0)
            alira.alira_helper.login(alira.url, "rterrones", "P@ssw0rd123.")
            excel_path = os.getcwd() + f"/resources/templates/seo/2022/12/KWR.xlsx"
            alira.alira_helper.get_kwr(excel_path)

            """ CASINO ONLINE """
            """first get our url base or references /casino-online /apuestas-deportivas"""
            alira.alira_helper.get_sheet_url_reference(1, 4, [
                        f"https://www.casinoatlnaticcity.com",
                        f"https://www.casinoatlanticcity.com",
                    ])

            references_1 = list(set(filter(lambda x: x != "/" and x != "", alira.alira_helper.sheets[1].data)))

            alira.alira_helper.get_sheet_url_reference(1, 5, [
                f"https://www.casinoatlnaticcity.com",
                f"https://www.casinoatlanticcity.com",
            ])

            references_1_1 = list(set(filter(lambda x: x != "/" and x != "", alira.alira_helper.sheets[1].data)))

            references_1 = references_1 + references_1_1
            #references_1 = ['/casino-online']

            alira.alira_helper.access_to_pages_tab()
            alira.alira_helper.get_sheet_target_urls(
                1, 4, 5,
                [
                    f"https://www.casinoatlnaticcity.com",
                    f"https://www.casinoatlanticcity.com",
                ])
            alira.alira_helper.target_urls = []
            for index, url in enumerate(alira.alira_helper.sheets[1].data):
                url.h1 = alira.alira_helper.get_sheet_row_data(1, [25], url.id)
                url.title = alira.alira_helper.get_sheet_row_data(1, [26], url.id)
                url.description = alira.alira_helper.get_sheet_row_data(1, [28], url.id)
                url.keywords = alira.alira_helper.get_sheet_row_data(1, [
                    7, 9, 11, 13, 15, 17, 19, 21, 23
                ], url.id)

                url.h1 = alira.alira_helper.trace_helper.contains_emoji(url.h1)
                url.title = alira.alira_helper.trace_helper.contains_emoji(url.title)
                url.description = alira.alira_helper.trace_helper.contains_emoji(url.description)
                url.keywords = alira.alira_helper.trace_helper.contains_emoji(url.keywords)
                # url.flag = True
                alira.alira_helper.target_urls.append(url)

            alira.alira_helper.trace_helper.log(text=f"------------------------------------------")
            alira.alira_helper.trace_helper.log(text=f"BUSCANDO LA SIGUIENTE DATA")
            alira.alira_helper.trace_helper.log(text=f"------------------------------------------")
            alira.alira_helper.trace_helper.log(text=f"{references_1_1}")
            for index, reference in enumerate(references_1):

                alira.alira_helper.trace_helper.log(text=f"------------------------------------------")
                alira.alira_helper.trace_helper.log(text=f"{index}. {reference}")
                alira.alira_helper.trace_helper.log(text=f"------------------------------------------")
                alira.alira_helper.url = reference
                alira.alira_helper.page = 1
                alira.alira_helper.iterate_main_datatable(save=True)
                while alira.alira_helper.page < alira.alira_helper.table_page_total:
                    alira.alira_helper.trace_helper.log(text=f"------------------------------------------")
                    alira.alira_helper.trace_helper.log(text=f"Pagina : {alira.alira_helper.page} |"
                                                             f" {alira.alira_helper.table_page_total}")
                    alira.alira_helper.trace_helper.log(text=f"------------------------------------------")
                    alira.alira_helper.iterate_main_datatable(save=True)
            """ """

            """" APUESTAS DEPORTIVAS """
            alira.alira_helper.get_sheet_url_reference(2, 2, [
                f"https://www.casinoatlnaticcity.com",
                f"https://www.casinoatlanticcity.com",
            ])
            references_2 = list(set(filter(lambda x: x != "/" and x != "", alira.alira_helper.sheets[2].data)))

            alira.alira_helper.get_sheet_target_urls(
                2,
                2,
                3,
                [
                    f"https://www.casinoatlnaticcity.com",
                    f"https://www.casinoatlanticcity.com",
                ])
            alira.alira_helper.target_urls = []
            for index, url in enumerate(alira.alira_helper.sheets[2].data):
                url.h1 = alira.alira_helper.get_sheet_row_data(2, [26], url.id)
                url.title = alira.alira_helper.get_sheet_row_data(2, [28], url.id)
                url.description = alira.alira_helper.get_sheet_row_data(2, [30], url.id)
                url.keywords = alira.alira_helper.get_sheet_row_data(2, [
                    9, 11, 13, 15, 17, 19, 21, 23, 25
                ], url.id)
                """-------------------------------------------------------------------"""
                url.h1 = alira.alira_helper.trace_helper.contains_emoji(url.h1)
                url.title = alira.alira_helper.trace_helper.contains_emoji(url.title)
                url.description = alira.alira_helper.trace_helper.contains_emoji(url.description)
                url.keywords = alira.alira_helper.trace_helper.contains_emoji(url.keywords)
                # url.flag = True
                alira.alira_helper.target_urls.append(url)

            for reference in references_2:
                alira.alira_helper.url = reference
                alira.alira_helper.page = 1
                alira.alira_helper.iterate_main_datatable(save=True)
                while alira.alira_helper.page < alira.alira_helper.table_page_total:
                    alira.alira_helper.iterate_main_datatable(save=True)

            alira.alira_helper = alira.alira_helper
            driver.close()
            print('-------------------- finished -----------------------')

        except (UnicodeDecodeError, StopIteration) as e:

            print('error: ', e)

        return self.alira_repository.set_seo_parameters_per_page(alira)

    def set_seo_redirection(self, alira: Alira):

        try:
            driver = None

            if alira.driver == 'Chrome':
                driver = webdriver.Chrome()
            elif alira.driver == 'Firefox':
                driver = webdriver.Firefox()
            elif alira.driver == 'Safari':
                driver = webdriver.Safari()
            elif alira.driver == 'Edge':
                driver = webdriver.Edge()

            tz = pytz.timezone('America/Bogota')
            directory_name = datetime.now(tz).strftime('%Y%m%d%H%M%S')

            alira.alira_helper = AliraHelper(driver, page=0)
            alira.alira_helper.login(alira.url, "rterrones", "P@ssw0rd123.")
            excel_path = os.getcwd() + f"/resources/templates/seo/2022/12/KWR.xlsx"
            alira.alira_helper.get_kwr(excel_path)

            alira.alira_helper.access_to_redirections()

            """ CASINO ONLINE """
            """first get our url base or references /casino-online /apuestas-deportivas"""
            alira.alira_helper.get_sheet_url_reference(1, 4, [
                f"https://www.casinoatlnaticcity.com",
                f"https://www.casinoatlanticcity.com",
            ])

            references_1 = list(set(filter(lambda x: x != "/" and x != "", alira.alira_helper.sheets[1].data)))

            alira.alira_helper.access_to_pages_tab()

            alira.alira_helper.get_sheet_target_urls(
                1, 4, 5,
                [
                    f"https://www.casinoatlnaticcity.com",
                    f"https://www.casinoatlanticcity.com",
                ])
            alira.alira_helper.target_urls = []
            for index, url in enumerate(alira.alira_helper.sheets[1].data):
                url.title = alira.alira_helper.get_sheet_row_data(1, [26], url.id)
                url.description = alira.alira_helper.get_sheet_row_data(1, [28], url.id)
                url.keywords = alira.alira_helper.get_sheet_row_data(1, [
                    7, 9, 11, 13, 15, 17, 19, 21, 23
                ], url.id)

                # url.flag = True
                alira.alira_helper.target_urls.append(url)

            for reference in references_1:
                alira.alira_helper.url = reference
                alira.alira_helper.page = 1
                alira.alira_helper.iterate_redirections_datatable_edit()
                while alira.alira_helper.page < alira.alira_helper.table_page_total:
                    alira.alira_helper.iterate_redirections_datatable_edit()
            """ """
            alira.alira_helper.iterate_redirections_datatable_save()

            driver.close()

        except (UnicodeDecodeError, StopIteration, Exception) as e:
            trace_helper = TraceHelper()

            print(f"Error on alira service: {trace_helper.get_trace_str(e)}")
        return self.alira_repository.set_seo_redirection(alira)

    def get_layouts(self, alira: Alira):
        pass

    def set_page_url(self, alira: Alira):
        return alira