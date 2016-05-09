TYPE_MAP = {
    'integer': 'integer',
    'character varying': 'string',
    'integer': 'integer',
    'timestamp with time zone': 'date',
    'timestamp': 'date',
    'date': 'date',
    'boolean': 'boolean',
    'bytea': 'binary',
    'jsonb': 'object',
    'json': 'object'
}


MAPPING_TEMPLATE = """{
    "mappings": {
        "%s": {
            "properties": %s
        }
    }
}
"""
