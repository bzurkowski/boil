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
from boil.exceptions import BoilError
from boil.utils.display import display


def main():
    args = docopt(__doc__)

    try:
        cmd.get_command(args).execute(args)
    except BoilError as ex:
        display("An error ocurred while executing the command: %s" % str(ex),
                color='red')
