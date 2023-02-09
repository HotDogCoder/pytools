from time import sleep

import json
import requests

from core.config import constants
from app.application.repositories_interfaces.screenshot_repository_interface import ScreenshotRepositoryInterface
from app.domain.models.screenshot import Screenshot
from core.database.mssql_connection import MssqlConnection


class ScreenshotRepository(ScreenshotRepositoryInterface):

    def __init__(self):
        super().__init__()

    def take_screenshot_of_servers_status_1(self, screenshot: Screenshot):

        url = constants.API_UPLOAD_SCREENSHOT
        multiple_files = []
        for image in screenshot.image_list:
            filename = image.split('/').pop()
            multiple_files.append(
                ('multi-files', (filename, open(image, 'rb'), 'image/png'))
            )

        r = requests.post(url, files=multiple_files)

        output = json.loads(r.content)

        paths = output['paths']

        with MssqlConnection() as cursor:
            cursor.execute("""
                SELECT *
                FROM mytable
            """)

            rows = cursor.fetchall()
            for row in rows:
                print(row)

        for file in paths:
            url = constants.API_WHATSAPP_WEB
            body = {
                'message': '',
                'number': f'{constants.API_WHATSAPP_WEB_BOT_TARGET_NUMBER_1}',
                'photo': f'{constants.API_WHATSAPP_WEB_BOT}/{file}'
            }
            r = requests.post(url, json=body)
            print(f'send whatsapp: {r.content}')
            sleep(5)

        url = constants.API_WHATSAPP_WEB
        body = {
            'message': '🤖 Buenas noches estimados, se envia print de monitoreo 🤖',
            'number': f'{constants.API_WHATSAPP_WEB_BOT_TARGET_NUMBER_1}',
            'photo': f''
        }
        r = requests.post(url, json=body)
        print(f'send whatsapp: {r.content}')
        sleep(5)

        return screenshot

    def test_atlantic_city_casino_and_sports(self, screenshot: Screenshot):
        pass

    with MssqlConnection() as cursor:
        cursor.execute("""
            select * from auth_user
        """)

        rows = cursor.fetchall()
        for row in rows:
            print(row)
