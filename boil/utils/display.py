import sys

from boil.utils import ansi


class Display:

    def display(self, msg, color=None, bold=False, stderr=False):
        msg = ansi.format(msg, color=color, bold=bold)
        msg += '\n'

        file_obj = sys.stdout
        if stderr:
            file_obj = sys.stderr

        file_obj.write(msg)
        file_obj.flush()

    def prompt(self, msg=None):
        if msg:
            msg = ansi.format(msg, bold=True)
        return raw_input(msg)
