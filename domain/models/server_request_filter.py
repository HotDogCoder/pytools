from domain.models.main_filter import MainFilter


class ServerRequestFilter(MainFilter):
    def __int__(self, date, text, number, method, request_type):
        super().__int__(date, text, number)
        self.method = method
        self.request_type = request_type

