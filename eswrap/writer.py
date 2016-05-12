from .scanner import Scanner
from . import MAPPING_TEMPLATE
import os


class Writer(object):

    def write_mapping(self, table_name, document_type, path=None):
        s = Scanner()
        fields = s.build_props(table_name)
        vals = {
            'map_name': table_name,
            'doc_type': document_type,
            'fields': fields
        }
        mapping = MAPPING_TEMPLATE % (vals)
        if not path:
            path = os.getcwd() + '/eswrap'
        path = path + '/{}_es_mapping.py'.format(table_name)
        with open(path, 'a') as f:
            f.write(mapping)
        return "Mapping written."
