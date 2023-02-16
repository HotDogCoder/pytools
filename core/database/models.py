from sqlalchemy import Column, Integer, String, DateTime, Text, text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

from core.database.mssql_connection import MssqlConnection
from core.util.debug.trace_helper import TraceHelper

Base = declarative_base()


class ReportTypesTable(Base):
    __tablename__ = 'report_types'
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(200))
    url = Column(String(1000))
    created_at = Column(DateTime)

class ReportsTable(Base):
    __tablename__ = 'reports'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200))
    code = Column(String(20))
    description = Column(String(200))
    created_at = Column(DateTime)

class ReportScreenshotsTable(Base):
    __tablename__ = 'report_screenshots'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200))
    path = Column(String(200))
    report_id = Column(Integer, ForeignKey('reports.id'))
    report_type_id = Column(Integer, ForeignKey('report_types.id'))
    created_at = Column(DateTime)