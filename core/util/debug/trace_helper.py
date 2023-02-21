import traceback
import emoji
import datetime

import pytz

from core.util.path.path_helper import PathHelper
from core.util.pdf.pdf_helper import PdfHelper


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

    def contains_emoji(self, text):
        emojis = emoji.emoji_list(text)
        for e in emojis:
            # print(e.emoji)
            # print(emoji.demojize(e))
            # hexcode = hex(ord(e.emoji))
            text = emoji.replace_emoji(text, replace=self.xml_escape)
        print(text)
        return text

    def log(self, text="", message=""):
        # Get current date and time
        path_helper = PathHelper()
        with open(f'{path_helper.get_project_root_path()}/storage/exportations/qa_report_log/qa_report_log_{self.now}.txt',
                  'a', encoding='utf-8') as file:
            self.log_lines.append(text)
            self.log_lines.append(message)
            file.write(f'{text}\n')
            file.write(f'{message}\n')

    # Define the maximum number of lines per page
    MAX_LINES_PER_PAGE = 20

    def write_to_qa_report_pdf_log(self):
        # Get current date and time
        path_helper = PathHelper()
        path = f'{path_helper.get_project_root_path()}/storage/exportations/qa_report_pdf/qa_report_pdf_{self.now}.pdf'
        pdf_helper = PdfHelper(path=path)
        pdf_helper.write_pdf(lines=self.log_lines)
        return path
