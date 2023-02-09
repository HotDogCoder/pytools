from sqlalchemy.orm import sessionmaker, Session

from core.database.models import ReportTypeTable


class ReportType:

    def __init__(self, id=0, description="", url="", created_at=None, base=None, engine=None):
        self.id = id
        self.description = description
        self.url = url
        self.created_at = created_at

        # def get(self, session):
        """Get a report type from the database by id."""
        # return session.query(self).get(self.id)
        # def delete(self):
        """Delete a report type from the database by id."""
        # report_type = self.base.session.query(self).get(self.id)
        # if report_type:
        #    self.base.session.delete(report_type)
        #    self.base.session.commit()
        # else:
        #    raise ValueError(f'Report type with id {self.id} not found.')
        # pass
