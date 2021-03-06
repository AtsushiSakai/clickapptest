import sys
import pathlib
import logging
import click_log
import click
import platform
logger = logging.getLogger(__name__)
click_log.basic_config(logger)

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
@click_log.simple_verbosity_option(logger)
def version():
    """ print version"""
    project_root_path = pathlib.Path(__file__).parent
    with open(project_root_path.joinpath("VERSION"), 'r') as fd:
        VERSION = fd.readline().rstrip('\n')
        click.echo(f"=== Version info ===")
        click.echo(f"clickapptest: {VERSION}")
        click.echo(f"OS: {platform.platform()}")
        click.echo(f"Python: {sys.version_info}")
        click.echo(f"Click: {click.__version__}")
        click.echo(f"click_log: {click_log.__version__}")


@clickapptest.command()
@click_log.simple_verbosity_option(logger)
def loggertest():
    logger.debug("aaa")
    logger.info("aaa")
    logger.warning("aaa")
    logger.error("aaa")


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
