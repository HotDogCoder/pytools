from abc import ABC, abstractmethod

from app.domain.models.screenshot import Screenshot


class ScreenshotRepositoryInterface(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def take_screenshot_servers_status_report(self, screenshot: Screenshot):
        return screenshot

