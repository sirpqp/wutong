import pymysql
from pymysql.cursors import Cursor, SSDictCursor, SSCursor, DictCursor
from pymysql.err import DatabaseError
from twisted.enterprise import adbapi
from twisted.internet import defer

from settings import (MYSQL_HOST, MYSQL_PORT, MYSQL_USER,
                          MYSQL_PWD, MYSQL_DATABASE)


def _connect(**kwargs):
    """获取连接"""
    kwargs.setdefault('host', MYSQL_HOST)
    kwargs.setdefault('port', MYSQL_PORT)
    kwargs.setdefault('user', MYSQL_USER)
    kwargs.setdefault('password', MYSQL_PWD)
    kwargs.setdefault('database', MYSQL_DATABASE)
    return pymysql.connect(**kwargs)


class MySqlClient(object):
    """基本的数据库处理类"""

    def __init__(self, **kwargs):
        self.conn = _connect(**kwargs)
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def execute(self, query, args=None, cursorclass=None):
        self._execute(query, args, cursorclass)
        self.conn.commit()

    def runquery(self, query, args=None, cursorclass=None):
        cur = self._execute(query, args, cursorclass)
        return cur.fetchall()

    def _execute(self, query, args=None, cursorclass=None):
        if cursorclass is not None:
            with self.conn.cursor(cursorclass) as c:
                c.execute(query, args)
                return c
        else:
            self.cursor.execute(query, args)
            return self.cursor

    def close(self):
        self.cursor.close()
        self.conn.close()

    @staticmethod
    def ssquery(query, args=None, cursorclass=SSDictCursor, db_params=None):
        """流式查询

        PS: 如果对数据流的操作间隔时间较长
            会导致连接中断等问题
            因此将整体流程放入死循环中，如果正常结束则退出
            否则继续执行

            可能会导致查询到重复的数据（视数据内容与 SQL 语句）

        """

        if not issubclass(cursorclass, SSCursor):
            raise TypeError(f'only accept subclasses of {SSCursor} or itself.')

        db_params = db_params or {}

        while True:

            conn = _connect(**db_params)
            cur = conn.cursor(cursorclass)

            try:
                cur.execute(query, args)
            except DatabaseError:
                cur.close()
                conn.close()
                raise
            try:
                yield from cur
            except Exception as e:
                print(e)
            else:
                cur.close()
                conn.close()
                break


class MysqlDbPool(object):
    """MySQL数据库连接池"""

    def __init__(self, host=MYSQL_HOST,
                 port=MYSQL_PORT,
                 user=MYSQL_USER,
                 pwd=MYSQL_PWD,
                 db=MYSQL_DATABASE,
                 min_conn=3,
                 max_conn=5):
        self.dbpool = adbapi.ConnectionPool(
            'pymysql',
            cp_reconnect=True,
            host=host,
            port=port,
            user=user,
            password=pwd,
            database=db,
            cp_min=min_conn,
            cp_max=max_conn
        )

    def runquery(self, query, args=None):
        """执行查询语句，返回查询结果
        行为与 pymysql.Cursor 执行的结果一样
        """
        return self.dbpool.runQuery(query, args=args)

    @defer.inlineCallbacks
    def execute(self, query, args=None):
        """执行sql语句"""
        yield self.dbpool.runInteraction(self._execute, query, args)

    def _execute(self, tx, query, args):
        """
        执行SQL语句

        :param doneback: 执行成功后的回调函数
        :param errback: 执行失败的回调函数 接收一个错误实例 e

        """
        tx.execute(query, args=args)

    def close(self):
        self.dbpool.close()
