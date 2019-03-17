import sqlite3
import os

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

    def query(self,sql,value=[]):
        if not self._cur:
            return None

        try:
            self._cur.execute(sql,value)
            return self._cur.fetchall()
        except:
            return None

    def create(self,sql):
        if not self._cur:
            return
        try:
            self._cur.execute(sql)
            self.commit()
        except:
            raise

    def insert(self,sql,value):
        if not self._cur:
            return
        try:
            self._cur.executemany(sql,value)
            self.commit()
        except:
            raise

    delete = insert

    def commit(self):
        try:
            self._conn.commit()
        except:
            self.rollback()

    def rollback(self):
        self._conn.rollback()

    def __del__(self):
        if self._cur:
            self._cur.close()
        if self._conn:
            self._conn.close()

    def close(self):
        self.__del__()


CREATE_ORDER = '''
    create table if not exists orders(
        id          integer primary key autoincrement,
        order_id    varchar(50) unique,
        car_id      varchar(50) default '',
        car_type    varchar(50)default '',
        car_user    varchar(50) default '',
        phone       varchar(20) default '',
        car_frame   varchar(50) default '',
        order_time  integer default 0,
        mile        integer default 0,
        remark      text default ''
    );
'''

CREATE_DETAIL = '''
    create table if not exists detail(
        id          integer primary key autoincrement,
        order_id    varchar(50) default '',
        project     varchar(50) default '',
        price       integer default 0,
        number      integer default 0,
        pay         integer default 0,
        remark      text default ''
    );
'''

DB_NAME = './guime.db'


def create_db(conn):
    conn.create(CREATE_ORDER)
    conn.create(CREATE_DETAIL)


if not os.path.exists(DB_NAME):
    DB_CONN = DB(DB_NAME)
    create_db(DB_CONN)
else:
    DB_CONN = DB(DB_NAME)


if __name__=='__main__':
    # DB_CONN.insert('insert into detail(order_id,project,pay,remark) values(?,?,?,?)',[['aa','aa','aa','aa']])
    # print(DB_CONN.query('select * from orders',[]))
    DB_CONN.insert('insert into orders(order_id,remark) values(?,?) on conflict(order_id) do update set phone=?,remark=?;',[('20190315001','12ss33221','gggg','ggg')])
    # DB_CONN.insert('''insert into orders(order_id,car_id,car_type,car_user,phone,car_frame,order_time,remark)
    #     values (?,?,?,?,?,?,?,?)
    #     on conflict(order_id)
    #     do update set car_id=?
    #     and car_type=?
    #     and car_user=?
    #     and phone=?
    #     and car_frame=?
    #     and order_time=?
    #     and remark=?''',[['20190315001', 'ff', 'ff', 'ff', 'ff', 'ffese', '2019-03-15', '', 'ff', 'ff', 'ff', 'ff', 'ffese', '2019-03-15', '']])


