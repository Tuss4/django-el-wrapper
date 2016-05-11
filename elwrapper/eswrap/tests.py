from unittest import TestCase
from .queries import CREATE_TEST_TABLE, DROP_TEST_TABLE
from . import db_conn



class ESWrapTest(TestCase):

    conn = db_conn()

    def setUp(self):
        with self.conn.cursor() as c:
            c.execute(CREATE_TEST_TABLE)

    def tearDown(self):
        with self.conn.cursor() as c:
            c.execute(DROP_TEST_TABLE)

    def test_eswrap(self):
        print("bruh")
