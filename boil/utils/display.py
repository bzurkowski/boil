import sys


class Display:

    def display(self, msg, stderr=False):
        file_obj = sys.stdout
        if stderr:
            file_obj = sys.stderr

        file_obj.write(msg)
        file_obj.flush()

    def prompt(self, msg):
        return raw_input(msg)
