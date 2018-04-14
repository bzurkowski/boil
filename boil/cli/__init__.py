"""Boil

Usage:
    boil list
    boil search <phrase>
    boil new <plate_name> [--target-dir=<dir>]
    boil -h | --help

Options:
    --target-dir=<dir>  Target directory where project files should be
                        populated.
"""

from docopt import docopt

from boil.cli import commands as cmd


def main():
    args = docopt(__doc__)

    command = get_command(args)
    command().execute(args)


def get_command(args):
    if args['list']:
        return cmd.ListPlates
    elif args['search']:
        return cmd.SearchPlates
    elif args['new']:
        return cmd.RenderPlate
