from app.application.repositories_interfaces.screenshot_repository_interface import ScreenshotRepositoryInterface
from app.domain.models.screenshot import Screenshot


class ScreenshotRepository(ScreenshotRepositoryInterface):
    def __init__(self):
        super().__init__()

    def take_screenshot_servers_status_report(self, screenshot: Screenshot):
        return screenshot

