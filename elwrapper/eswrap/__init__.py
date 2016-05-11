import os
import psycopg2
from urllib.parse import urlparse

DATABASE_URL = os.getenv('DATABASE_URL')
assert DATABASE_URL

TYPE_MAP = {  # Maps PostgreSQL data type keys to Elasticsearch data type vals
    'integer': 'integer',
    'character varying': 'string',
    'text': 'string',
    'integer': 'integer',
    'timestamp with time zone': 'date',
    'timestamp': 'date',
    'date': 'date',
    'boolean': 'boolean',
    'bytea': 'binary',
    'jsonb': 'object',
    'json': 'object'
}


MAPPING_TEMPLATE = """%(map_name)s_mapping = {
    "mappings": {
        "%(doc_type)s": {
            "properties": %(fields)s
        }
    }
}
"""


def db_conn():
    parts = urlparse(DATABASE_URL)
    return psycopg2.connect(
        database=parts.path.strip('/'), user=parts.username,
        password=parts.password, port=parts.port, host=parts.hostname)
