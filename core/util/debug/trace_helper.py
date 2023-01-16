import traceback


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
