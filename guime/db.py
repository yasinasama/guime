import sqlite3

class DB:
    def __init__(self,dbpath):
        self.db_path = dbpath
        self._conn = None
        self._cur = None

        self._connect()

    def _connect(self):
        if not self._conn:
            self._conn = sqlite3.connect(self.db_path)
            self._cur = self._conn.cursor()

    def query(self,sql):
        if not self._cur:
            return None

        try:
            self._cur.execute(sql)
        except:
            return None

    def __del__(self):
        if self._cur:
            self._cur.close()
        if self._conn:
            self._conn.close()

    def close(self):
        self.__del__()


DB_CONN = DB('./guime.db')

