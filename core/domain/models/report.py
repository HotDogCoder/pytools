class Report:

    def __init__(self, id=0, name="", code="", description="", created_at=None, base=None, engine=None):
        self.id = id
        self.name = name
        self.code = code
        self.description = description
        self.created_at = created_at
        self.screenshots = []