from unittest import TestCase
from . import db_conn
from .queries import CREATE_TEST_TABLE, DROP_TEST_TABLE
from .writer import Writer
from .scanner import Scanner
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
        filename = "test_table_es_mapping.py"
        files = os.listdir('{}/eswrap'.format(os.getcwd()))
        if filename in files:
            cmd = "rm {}/eswrap/{}".format(os.getcwd(), filename)
            subprocess.run([cmd], shell=True, check=True)

    def test_writer(self):
        w = Writer()
        w.write_mapping('test_table', 'test_document')
        files = os.listdir('{}/eswrap'.format(os.getcwd()))
        self.assertIn('test_table_es_mapping.py', files)

    def test_scanner(self):
        s = Scanner()
        props = s.build_props('test_table')
        print(s.get_table_schema('test_table'))
        print(props)
        self.assertEqual(props['id'], dict(type='integer'))
        self.assertEqual(props['foo'], dict(type='string'))
        self.assertEqual(props['bar'], dict(type='string'))
