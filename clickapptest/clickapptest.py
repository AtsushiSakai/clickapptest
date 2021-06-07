import click
import pathlib

try:  # for pip package
    from clickapptest.lib.tool1 import tool1
    from clickapptest.lib.tool2 import tool2
    from clickapptest.lib.tool3 import tool3
except ModuleNotFoundError:  # for local call
    from lib.tool1 import tool1
    from lib.tool2 import tool2
    from lib.tool3 import tool3


@click.group()
def clickapptest():
    """
    This is a sample click test (v{VERSION})
    """
    pass


@clickapptest.command()
def version():
    """ print version"""
    project_root_path = pathlib.Path(__file__).parent
    with open(project_root_path.joinpath("VERSION"), 'r') as fd:
        VERSION = fd.readline().rstrip('\n')
        click.echo(f"v{VERSION}")


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


@clickapptest.command()
@click.argument('mode', type=click.Choice(['CSV', 'JSON'], case_sensitive=False))
def run_test3(mode):
    """
    This is a command line tool for run test2
    """
    tool3.run(mode)


if __name__ == '__main__':
    clickapptest()
