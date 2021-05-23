import click

from src.tool1 import tool1
from src.tool2 import tool2


@click.group()
def clickapptest():
    """
    This is a sample click test
    """
    pass


@clickapptest.command()
@click.argument('name')
def run_test1(name):
    """
    run test1

    NAME: name
    """
    tool1.run(name)


@clickapptest.command()
@click.option('--num', '-n', default=1)
def run_test2(num):
    """
    This is a command line tool for run test2
    """
    tool2.run(num)


if __name__ == '__main__':
    clickapptest()