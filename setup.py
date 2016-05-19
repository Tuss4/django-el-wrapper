from setuptools import setup


setup(
    name="es-map-writer",
    version='0.1',
    packages=['es_map_writer'],
    py_modules=['es_map_writer'],
    install_requires=[
        'click==6.6',
    ],
    entry_points='''
        [console_scripts]
        mapwrtr=es_map_writer.command:cli
    ''',
)
