import pyodbc

from core.config import constants


class MssqlConnection:

    def __init__(self, server=constants.DB_HOST,
                 database=constants.DB_NAME, username=constants.DB_USER,
                 password=constants.DB_PASSWORD):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = pyodbc.connect(
            f'DRIVER={constants.DB_DRIVER};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' +
            self.username + ';PWD=' + self.password)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, type, value, traceback):
        self.cursor.close()
        self.conn.close()
