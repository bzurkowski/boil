import os

from mock import patch
from six.moves import StringIO
import unittest

from boil.cli import commands as cmd
from boil.utils.file_utils import temp_dir


class CommandsTest(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    @patch("boil.utils.display.input")
    def test_run_plate(self, mock_input, mock_stdout):
        mock_input.return_value = "foo"

        with temp_dir() as target_dir:
            args = {"<plate_name>": "python_package", "--target-dir": target_dir}
            command = cmd.RunPlate()
            command.execute(args)
            result = mock_stdout.getvalue()

            self.assertIn("foo", os.listdir(target_dir))

            self.assertIn("Initializing new Python package", result)
            self.assertIn("Done!", result)

    @patch("sys.stdout", new_callable=StringIO)
    def test_list_plates(self, mock_stdout):
        args = {}
        command = cmd.ListPlates()
        command.execute(args)
        result = mock_stdout.getvalue()
        self.assertIn("python_package", result)
        self.assertIn("ansible_role", result)

    @patch("sys.stdout", new_callable=StringIO)
    def test_search_plates(self, mock_stdout):
        args = {"<phrase>": "py"}
        command = cmd.SearchPlates()
        command.execute(args)
        result = mock_stdout.getvalue()
        self.assertIn("python_package", result)
        self.assertNotIn("ansible_role", result)

    @patch("sys.stdout", new_callable=StringIO)
    def test_search_plates_not_found(self, mock_stdout):
        args = {"<phrase>": "unfindable_package"}
        command = cmd.SearchPlates()
        command.execute(args)
        result = mock_stdout.getvalue()
        self.assertIn("No plates found.", result)
