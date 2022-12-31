from time import sleep

import constants
from app.application.repositories_interfaces.screenshot_repository_interface import ScreenshotRepositoryInterface
from app.domain.models.screenshot import Screenshot
import requests, json

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
            body = {'message': '', 'number': '51945633041-1464183842@g.us', 'photo': f'{constants.API_WHATSAPP_WEB_BOT}/{file}'}
            r = requests.post(url, json=body)
            print(f'send whatsapp: {r.content}')
            sleep(5)

        url = constants.API_WHATSAPP_WEB
        body = {'message': '🤖 Buenas noches estimados, se envia print de monitoreo 🤖', 'number': '51945633041-1464183842@g.us',
                'photo': f''}
        r = requests.post(url, json=body)
        print(f'send whatsapp: {r.content}')
        sleep(5)

        return screenshot

    def test_atlantic_city_casino_and_sports(self, screenshot: Screenshot):
        pass


