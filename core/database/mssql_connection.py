import urllib.parse

from core.config import constants
from sqlalchemy import create_engine


class MssqlConnection:

    def __init__(self,
                 driver=constants.DB_DRIVER,
                 host=constants.DB_HOST,
                 port=constants.DB_PORT,
                 database=constants.DB_NAME,
                 username=constants.DB_USER,
                 password=constants.DB_PASSWORD):
        self.driver = driver
        self.host = host
        # self.port = port
        self.database = database
        self.username = username
        self.password = password
        self.conn = None
        self.cursor = None
        password = urllib.parse.quote_plus(password)
        self.connection_string = f"mssql+pyodbc://{username}:{password}@{host}" \
                                 f"/{database}?driver=SQL+Server"
        self.engine = create_engine(self.connection_string)

    def connect(self):
        connection = self.engine.connect()
        return connection

    def close(self, connection):
        connection.close()
