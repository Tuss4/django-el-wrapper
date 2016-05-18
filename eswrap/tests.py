from unittest import TestCase
from . import db_conn, es_conn
from .queries import CREATE_TEST_TABLE, DROP_TEST_TABLE
from .writer import Writer
from .scanner import Scanner
import os
import subprocess
import time
from importlib import import_module


class ESWrapTest(TestCase):

    conn = db_conn()
    es = es_conn()

    def setUp(self):
        with self.conn.cursor() as c:
            c.execute(CREATE_TEST_TABLE)

    def tearDown(self):
        with self.conn.cursor() as c:
            c.execute(DROP_TEST_TABLE)
        filename = "foo_table_es_mapping.py"
        files = os.listdir('{}/eswrap'.format(os.getcwd()))
        if filename in files:
            cmd = "rm {}/eswrap/{}".format(os.getcwd(), filename)
            subprocess.run([cmd], shell=True, check=True)
        # Add method for clearing indices.
        if self.es.indices.exists(index=['test_index']):
            self.es.indices.delete(index=['test_index'])

    def test_writer(self):
        w = Writer()
        w.write_mapping('foo_table', 'foo_document')
        files = os.listdir('{}/eswrap'.format(os.getcwd()))
        self.assertIn('foo_table_es_mapping.py', files)
        module = import_module('eswrap.foo_table_es_mapping')
        self.assertTrue(hasattr(module, 'foo_table_mapping'))
        mapping = getattr(module, 'foo_table_mapping')
        expected = {
            'mappings': {
                'foo_document': {
                    'properties': {
                        'foo': {'type': 'string'},
                        'id': {'type': 'integer'},
                        'bar': {'type': 'string'}
                    }
                }
            }
        }
        self.assertEqual(mapping, expected)

    def test_scanner(self):
        s = Scanner()
        props = s.build_props('foo_table')
        self.assertEqual(props['id'], dict(type='integer'))
        self.assertEqual(props['foo'], dict(type='string'))
        self.assertEqual(props['bar'], dict(type='string'))

    def test_create_index(self):
        w = Writer()
        w.write_mapping('foo_table', 'foo_document')
        module = import_module('eswrap.foo_table_es_mapping')
        mapping = getattr(module, 'foo_table_mapping')
        self.es.indices.create(index='test_index', body=mapping)
        time.sleep(2)
        self.assertTrue(self.es.indices.exists(index=['test_index']))
        actual_mapping = self.es.indices.get_mapping(
            index=['test_index'], doc_type=['foo_document'])
        exp_mapping = {
            'mappings': {
                'foo_document': {
                    'properties': {
                        'foo': {'type': 'string'},
                        'id': {'type': 'integer'},
                        'bar': {'type': 'string'}
                    }
                }
            }
        }
        self.assertEqual(actual_mapping['test_index'], exp_mapping)
