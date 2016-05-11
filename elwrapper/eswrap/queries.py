GET_TABLE_SCHEMA = """
SELECT column_name, data_type
FROM   information_schema.columns
WHERE  table_name = %s;
"""


CREATE_TEST_TABLE = """
CREATE TABLE test_table(
    id  SERIAL PRIMARY KEY,
    foo TEXT,
    bar TEXT
);
"""

DROP_TEST_TABLE = """
DROP TABLE IF EXISTS test_table CASCADE;
"""
