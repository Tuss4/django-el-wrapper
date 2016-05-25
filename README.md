# ES Map Writer

[![Build Status](https://travis-ci.org/Tuss4/es-map-writer.svg?branch=master)](https://travis-ci.org/Tuss4/es-map-writer)

A command line tool that writes an Elasticsearch index mapping for a PostgreSQL database.

+ Compatible with:
 + Python 3.5
 + Elasticsearch 2.3.2
 + PostgreSQL 9+

## How To Use:

 For help:  
 + `mapwrtr --help`

 Help menu:
 ```
 Usage: mapwrtr [OPTIONS]

 Options:
   --database-url TEXT   Postgres URI.
   --file-path TEXT      Output file destination folder.
   --table-name TEXT     Postgres table the mapping is being written for.
   --index-name TEXT     Elasticsearch index name. Will default to the table
                         name if blank.
   --document-type TEXT  Elasticsearch document type.
   --help                Show this message and exit.
 ```

File name format: `[table_name]_es_mapping.py`

Example:
We have a table named "superheroes" that we plan on creating an index for on an Elasticsearch node.
`mapwrtr --database-url=postgres://pguser:pgpass@localhost:5432/mydb --file-path=/home/me/myapps/mapping --table-name=superheroes --document-type=superhero_doc`

This will generate a mapping for my index in `/home/me/myapps/mapping/superheroes_es_mapping.py`

Now when I'm creating (or updating) my superheroes index, I can import the mapping that was generated. If I need to add some custom analyzers and tokenizers, I can do that too.


**Note(s):**
+ `--database-url` must be in the Postgres URI format `postgres://user:pass@host:port/database`
+ `--file-path` must be an absolute path eg `/home/me/Documents/myapp/esmapping`
