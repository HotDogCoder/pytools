import traceback

from core.util.path.path_helper import PathHelper


class TraceHelper:
    def __init__(self):
        self.message = ""
        self.trace = ""
        self.image = ""

    @staticmethod
    def get_trace_str(e):
        traceback_str = ''.join(traceback.format_tb(e.__traceback__))
        return traceback_str

    @staticmethod
    def trace_str(self, e):
        traceback_str = ''.join(traceback.format_tb(e.__traceback__))
        self.trace = traceback_str

    @staticmethod
    def log(text="", message=""):
        # Open the file in append mode
        path_root = f"{PathHelper.get_project_root_path()}resources/exportations/qa_report_1.txt"
        with open(path_root, "a") as file:
            # Add a new line to the end of the file
            file.write(f"\nTEXT|{text}")
            file.write(f"\nMESSAGE|{message}")