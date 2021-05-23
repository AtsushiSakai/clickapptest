from setuptools import setup

setup(
    name='clickapptest',
    version='0.1.0',
    py_modules=['clickapptest'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        clickapptest=clickapptest:cli
    ''',
)