import psycopg2
import os
from urllib.parse import urlparse
from .queries import GET_TABLE_SCHEMA
from . import TYPE_MAP


DATABASE_URL = os.getenv('DATABASE_URL')
assert DATABASE_URL


def db_conn():
    parts = urlparse(DATABASE_URL)
    return psycopg2.connect(
        database=parts.path.strip('/'), user=parts.username,
        password=parts.password, port=parts.port, host=parts.hostname)


class Scanner(object):

    conn = db_conn()

    def get_table_schema(self, table_name):
        r = None
        try:
            with self.conn.cursor() as c:
                c.execute(GET_TABLE_SCHEMA, (table_name, ))
                r = c.fetchall()
        except Exception:
            pass
        return r

    def build_props(self, table_name):
        cols = self.get_table_schema(table_name)
        props = {}
        for col in cols:
            props[col[0]] = dict(type=TYPE_MAP[col[1]])
        return props
