# -*- coding: utf-8 -*-

"""Console script for Sep19Example."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for Sep19Example."""
    click.echo("Replace this message by putting your code into "
               "Sep19Example.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
