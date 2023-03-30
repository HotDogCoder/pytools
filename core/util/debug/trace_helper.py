import traceback
import datetime
import re
import pytz

from core.util.path.path_helper import PathHelper


class TraceHelper:
    def __init__(self):
        self.message = ""
        self.trace = ""
        self.image = ""
        self.log_lines = []
        tz = pytz.timezone('America/Bogota')
        self.now = datetime.datetime.now(tz).strftime('%Y%m%d%H%M%S')

    @staticmethod
    def get_trace_str(e):
        traceback_str = ''.join(traceback.format_tb(e.__traceback__))
        return traceback_str

    @staticmethod
    def xml_escape(chars, data_dict):
        return chars.encode('ascii', 'xmlcharrefreplace').decode()

    def log(self, text="", message=""):
        # Get current date and time
        path_helper = PathHelper()
        path = f'{path_helper.get_project_root_path()}/storage/logs'
        folder_path = path_helper.create_directory(path)
        with open(f'{folder_path}/log_{self.now}.html',
                  'a', encoding='utf-8') as file:
            self.log_lines.append(text)
            self.log_lines.append(message)
            file.write(f'{text}\n')
            file.write(f'{message}\n')

    def extract_url_from_styles(self, text=""):
        if text != "":
            url_re = re.search(r'url\((.*?)\)', text)
            if url_re is not None:
                url = url_re.group(1)
                return url
        else:
            return "ERROR"