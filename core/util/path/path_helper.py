from pathlib import Path
import os


class PathHelper:
    def __init__(self):
        pass

    @staticmethod
    def get_project_root_path() -> Path:
        return Path(__file__).parent.parent.parent.parent

    @staticmethod
    def create_directory(path):
        if not os.path.exists(path):
            os.makedirs(path)
