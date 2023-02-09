from datetime import datetime, timedelta
from time import sleep

import json
import requests

from core.config import constants
from app.application.repositories_interfaces.screenshot_repository_interface import ScreenshotRepositoryInterface
from app.domain.models.screenshot import Screenshot


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

        current_time = datetime.now()
        night_time = datetime(current_time.year, current_time.month, current_time.day, 18, 30, 0)
        good_time = datetime(current_time.year, current_time.month, current_time.day, 16, 20, 0)
        afternoon_time = datetime(current_time.year, current_time.month, current_time.day, 12, 0, 0)
        morning_time = datetime(current_time.year, current_time.month, current_time.day, 6, 0, 0)

        # time_diff = current_time - specific_time

        if morning_time <= current_time < afternoon_time:
            hello = "Estimados buenos dias"
        if afternoon_time <= current_time < good_time:
            hello = "Estimados buenas tardes"
        if good_time <= current_time < night_time:
            hello = "Estimados tengan muy buenas tardes"
        if current_time > night_time or current_time < morning_time:
            hello = "Estimados buenas noches"

        url = constants.API_WHATSAPP_WEB
        body = {
            'message': f'🤖 {hello}, se envia print de monitoreo. 🤖',
            'number': f'{constants.API_WHATSAPP_WEB_BOT_TARGET_NUMBER_1}',
            'photo': f''
        }
        r = requests.post(url, json=body)
        print(f'send whatsapp: {r.content}')
        sleep(5)

        return screenshot

    def test_atlantic_city_casino_and_sports(self, screenshot: Screenshot):
        pass

