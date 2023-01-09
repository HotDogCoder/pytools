import traceback


class TraceHelper:
    def __init__(self):
        self.name = "Trace Helper"

    def get_trace_str(self, e):
        traceback_str = ''.join(traceback.format_tb(e.__traceback__))
        return traceback_str

