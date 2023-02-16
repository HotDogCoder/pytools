class ReportType:

    def __init__(self, id=0, description="", url="", created_at=None, base=None, engine=None):
        self.id = id
        self.description = description
        self.url = url
        self.created_at = created_at
        self.screenshots = []
