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
                ('url internas',
                 'https://grafana.acity.com.pe/d/hT18KZz4z/monitoreo-url-internas?orgId=1&refresh=5s&from=now-1h&to=now'),
                (
                    'estado replica',
                    'https://grafana.acity.com.pe/d/LLSTg4zVz/estado-replica?orgId=1&refresh=5s&from=now-15m&to=now'),
                ('dashboard casino online',
                 'https://grafana.acity.com.pe/d/DjMVuiMVk/dashboard-casino-online?orgId=1&refresh=5s&from=now-15m&to'
                 '=now'),
                ('atlantic express',
                 'https://grafana.acity.com.pe/d/-JFbnTn99/atlantic-express?orgId=1&refresh=5s&from=now-30m&to=now'),
                ('crm cloud',
                 'https://grafana.acity.com.pe/d/-JFbn66n4z/crmcloud?orgId=1&refresh=5s&from=now-30m&to=now'),
                ('websol', 'https://grafana.acity.com.pe/d/-JFbnTn411/websol?orgId=1&refresh=5s&from=now-30m&to=now'),
                ('genesys y crm cloud',
                 'https://grafana.acity.com.pe/d/-JFbnT664z/genesys-y-crmcloud?orgId=1&refresh=5s&from=now-30m&to=now'),
                ('total competencias',
                 'https://grafana.acity.com.pe/d/ac0OemdVk/total-competencias?orgId=1&refresh=5s&from=now-15m&to=now'),
                ('views nzqp', 'https://grafana.acity.com.pe/d/XYVkz7V4k/views-nzgp?orgId=1&refresh=5s'),
                ('atlantic express diario',
                 'https://grafana.acity.com.pe/d/k6RHcLo4k/atlantic-express-diario?orgId=1&refresh=5s&var-Fecha=['
                 'GETDATE]&from=now-15m&to=now')
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
