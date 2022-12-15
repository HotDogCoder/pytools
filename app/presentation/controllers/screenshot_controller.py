from app.application.services.screenshot_service import ScreenshotService
from app.domain.models.screenshot import Screenshot


class ScreenshotController:

    def __init__(self):
        self.screenshot_service = ScreenshotService()

    def take_screenshot_servers_status_report(self, screenshot: Screenshot):
        return self.screenshot_service.take_screenshot_servers_status_report(screenshot)

