from .scanner import Scanner
from . import MAPPING_TEMPLATE
import os


class Writer(object):

    def write_mapping(self, table_name, document_type, path=None):
        s = Scanner()
        fields = s.build_props(table_name)
        mapping = MAPPING_TEMPLATE % (document_type, fields)
        if not path:
            path = os.getcwd()
        path = path + '/es_mapping.py'
        with open(path, 'a') as f:
            f.write(mapping)
        return "Mapping written."
