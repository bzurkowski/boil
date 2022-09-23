import math
import sys

from six.moves import input

from boil.utils import ansi


def display(msg, color=None, bold=False, stderr=False):
    msg = ansi.format(msg, color=color, bold=bold)
    msg += "\n"

    file_obj = sys.stdout
    if stderr:
        file_obj = sys.stderr

    file_obj.write(msg)
    file_obj.flush()


def display_list(obj, cols=4, columnwise=True, gap=10):
    slist = [str(item) for item in obj]
    num_items = len(slist)

    cols = min(cols, num_items)
    max_len = max([len(item) for item in slist])

    if columnwise:
        cols = int(math.ceil(float(num_items) / cols))

    plist = [slist[i : i + cols] for i in range(0, num_items, cols)]

    if columnwise:
        plist[-1].extend([""] * (num_items - len(plist[-1])))
        plist = zip(*plist)

    segments = ["".join([c.ljust(max_len + gap) for c in p]) for p in plist]
    msg = "\n".join(segments)
    display(msg)


def prompt(msg=None):
    if msg:
        msg = ansi.format(msg, bold=True)
    return input(msg)
