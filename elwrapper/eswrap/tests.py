from unittest import TestCase
from . import db_conn
from .queries import CREATE_TEST_TABLE, DROP_TEST_TABLE
from .writer import Writer
import os
import subprocess


class ESWrapTest(TestCase):

    conn = db_conn()

    def setUp(self):
        with self.conn.cursor() as c:
            c.execute(CREATE_TEST_TABLE)

    def tearDown(self):
        with self.conn.cursor() as c:
            c.execute(DROP_TEST_TABLE)
        cmd = "rm {}/eswrap/test_table_es_mapping.py".format(os.getcwd())
        subprocess.run([cmd], shell=True, check=True)

    def test_eswrap(self):
        w = Writer()
        w.write_mapping('test_table', 'test_document')
        files = os.listdir('{}/eswrap'.format(os.getcwd()))
        self.assertIn('test_table_es_mapping.py', files)
