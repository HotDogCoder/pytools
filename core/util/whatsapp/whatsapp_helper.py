from time import sleep
import json
import requests
from core.config import constants


class WhatsappHelper:

    def __init__(self, number):
        self.number = number
        pass

    def send_message(self, message, photo):
        url = constants.API_WHATSAPP_WEB
        body = {
            'message': message,
            'number': f'{self.number}',
            'photo': f'{constants.API_WHATSAPP_WEB_BOT}/{photo}'
        }
        r = requests.post(url, json=body)
        print(f'send whatsapp: {r.content}')
        sleep(5)

    @staticmethod
    def update_file(paths, mime='image/png'):
        url = constants.API_UPLOAD_SCREENSHOT
        multiple_files = []

        for path in paths.image_list:
            filename = path.split('/').pop()
            multiple_files.append(
                ('multi-files', (filename, open(path, 'rb'), mime))
            )

        r = requests.post(url, files=multiple_files)

        output = json.loads(r.content)

        paths = output['paths']
        return paths
