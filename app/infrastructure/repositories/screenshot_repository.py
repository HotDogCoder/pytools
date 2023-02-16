from datetime import datetime
from time import sleep

import json
import requests
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm import sessionmaker

from core.config import constants
from app.application.repositories_interfaces.screenshot_repository_interface import ScreenshotRepositoryInterface
from app.domain.models.screenshot import Screenshot
from core.database.models import ReportTypesTable, ReportScreenshotsTable
from core.database.models import ReportsTable
from core.database.mssql_connection import MssqlConnection
from core.domain.models.report_screenshot import ReportScreenshot
from core.domain.models.report_type import ReportType
from core.util.debug.trace_helper import TraceHelper

engine = MssqlConnection().engine
session_class = sessionmaker(bind=engine)

class ScreenshotRepository(ScreenshotRepositoryInterface):

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_all_report_types():
        session = session_class()
        report_types = session.query(ReportTypesTable).all()
        session.close()

        return report_types

    @staticmethod
    def add_report(name, code, description):
        session = session_class()
        report_table = ReportsTable()
        report_table.name = name
        report_table.code = code
        report_table.description = description
        report_table.created_at = datetime.now()
        session.add(report_table)

        session.commit()

        report_table_response = ReportType()
        report_table_response.id = report_table.id
        report_table_response.name = report_table.name
        report_table_response.code = report_table.code
        report_table_response.description = report_table.description
        report_table_response.created_at = report_table.created_at

        session.close()

        return report_table_response

    @staticmethod
    def add_report_screenshot(name, path, report_id, report_type_id):
        session = session_class()
        report_screenshot_table = ReportScreenshotsTable()
        try:
            report_screenshot_table.name = name
            report_screenshot_table.path = path
            report_screenshot_table.report_id = report_id
            report_screenshot_table.report_type_id = report_type_id
            report_screenshot_table.created_at = datetime.now()
            session.add(report_screenshot_table)

            session.commit()
        except (SQLAlchemyError, IntegrityError) as e:

            print(TraceHelper().get_trace_str(e))

        report_screenshot_table_response = ReportScreenshot()
        report_screenshot_table_response.id = report_screenshot_table.id
        report_screenshot_table_response.path = report_screenshot_table.path
        report_screenshot_table_response.report_id = report_screenshot_table.report_id
        report_screenshot_table_response.report_type_id = report_screenshot_table.report_type_id
        report_screenshot_table_response.created_at = report_screenshot_table.created_at

        session.close()

        return report_screenshot_table_response

    def upload_screeshots(self, report_screenshot: ReportScreenshot):
        url = constants.API_UPLOAD_SCREENSHOT
        multiple_files = []

        filename = report_screenshot.path.split('/').pop()
        multiple_files.append(
            ('multi-files', (filename, open(report_screenshot.path, 'rb'), 'image/png'))
        )
        r = requests.post(url, files=multiple_files)
        output = json.loads(r.content)
        paths = output['paths']
        report_screenshot.path = paths[0]

        report_screenshot = self.add_report_screenshot(
            name=f"screenshot_{report_screenshot.report_id}_{report_screenshot.report_type_id}",
            path=report_screenshot.path,
            report_id=report_screenshot.report_id,
            report_type_id=report_screenshot.report_type_id
        )

        return report_screenshot

    def take_screenshot_of_servers_status_1(self, screenshot: Screenshot):
        # report_type = ReportType(base=self.base.declarative_base)
        paths = []
        for index, report_type in enumerate(screenshot.trash):
            for report_screenshot in report_type.screenshots:
                new_report_screenshot = self.upload_screeshots(report_screenshot)
                paths.append(new_report_screenshot.path)

        # paths = []

        current_datetime = datetime.now()

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
        # session.close()
        return screenshot

    def test_atlantic_city_casino_and_sports(self, screenshot: Screenshot):
        pass
