from setuptools import setup, find_packages
import pathlib
project_root_path = pathlib.Path(__file__).parent

# read VERSION
with open(project_root_path.joinpath("VERSION"), 'r') as fd:
    VERSION = fd.readline().rstrip('\n')

setup(
    name='clickapptest',
    version=VERSION,
    url="https://github.com/AtsushiSakai/clickapptest",
    author="Atsushi Sakai",
    author_email="asakaig@gmail.com",
    maintainer='Atsushi Sakai',
    maintainer_email='asakaig@gmail.com',
    description="A click based cli app test",
    python_requires='>3.7.0',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['clickapptest'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        clickapptest=clickapptest:clickapptest
    ''',
)
