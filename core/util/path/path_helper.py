from pathlib import Path


class PathHelper:
    def __init__(self):
        pass

    @staticmethod
    def get_project_root_path() -> Path:
        return Path(__file__).parent.parent.parent.parent
