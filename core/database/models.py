from sqlalchemy import Column, Integer, String, DateTime, Text, text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class ReportTypeTable(Base):
    __tablename__ = 'report_types'
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(200))
    url = Column(String)
    created_at = Column(DateTime, server_default=text('getdate()'))


class ReportTable(Base):
    __tablename__ = 'reports'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=None))
    code = Column(String(20))
    description = Column(Text)
    created_at = Column(DateTime, server_default=text('getdate()'))


class ReportScreenshotTable(Base):
    __tablename__ = 'report_screenshots'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    path = Column(String(length=None))
    report_id = Column(Integer, ForeignKey('reports.id'))
    report_type_id = Column(Integer, ForeignKey('report_types.id'))
    created_at = Column(DateTime)

