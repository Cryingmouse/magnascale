import click

from magnascale.command import CONTEXT_SETTINGS
from magnascale.command.lisa.web_service import web_service


@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    pass


main.add_command(web_service)
