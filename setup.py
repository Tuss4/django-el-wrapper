from setuptools import setup


setup(
    name="es-map-writer",
    version='0.1',
    author='TJ Soptame',
    author_email='tj.soptame@gmail.com',
    description='A command line tool that writes an Elasticsearch index mapping for a PostgreSQL database table.',
    url='https://github.com/tuss4/es-map-writer',
    packages=['es_map_writer'],
    py_modules=['es_map_writer'],
    install_requires=[
        'click==6.6',
        'psycopg2==2.6.1',
    ],
    entry_points='''
        [console_scripts]
        mapwrtr=es_map_writer.command:cli
    ''',
)
