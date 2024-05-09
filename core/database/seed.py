from sqlalchemy.orm import sessionmaker

from core.database.mssql_connection import MssqlConnection
from core.domain.models.base import Base
from core.database.models.report_type_table import ReportTypeTable
from core.util.debug.trace_helper import TraceHelper

engine = MssqlConnection().engine
try:
    Base.metadata.create_all(engine)
except (Exception, BaseException) as e:
    trace_helper = TraceHelper
    print(trace_helper.get_trace_str(e))

session_class = sessionmaker(bind=engine)


class ReportTypesSeed:

    def __init__(self, data=None):
        if data is None:

            new_data = [
                ('monitoreo', 'https://monitoreo.acity.com.pe/apps/platform/dashboard/3'),
            ]

            self.insert_data(new_data)

        else:
            self.data = data
            self.insert_data(self.data)

    @classmethod
    def insert_data(cls, data):
        session = session_class()
        for report in data:
            session.add(ReportTypeTable(description=report[0], url=report[1]))
        session.commit()
        session.close()
