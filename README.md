# ES Map Writer

[![Build Status](https://travis-ci.org/Tuss4/es-map-writer.svg?branch=master)](https://travis-ci.org/Tuss4/es-map-writer)

A module that writes an Elasticsearch index mapping for a PostgreSQL database.

**Note(s):**
+ A `DATABASE_URL` environmental variable must be specified.
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
  --file-path TEXT      Output file destination.
  --table-name TEXT     Postgres table the mapping is being written for.
  --index-name TEXT     Elasticsearch index name. Will default to the table
                        name if blank.
  --document-type TEXT  Elasticsearch document type.
  --help                Show this message and exit.
```
