import os
from StringIO import StringIO
from mock import patch
import unittest

from boil.cli import commands as cmd
from boil.utils.file_utils import temp_dir


class CommandsTest(unittest.TestCase):

    @patch("sys.stdout", new_callable=StringIO)
    @patch("__builtin__.raw_input")
    def test_run_plate(self, mock_raw_input, mock_stdout):
        mock_raw_input.return_value = 'foo'

        with temp_dir() as target_dir:
            args = {'<plate_name>': 'python_package',
                    '--target-dir': target_dir}
            command = cmd.RunPlate()
            command.execute(args)
            result = mock_stdout.getvalue()

            self.assertIn('foo', os.listdir(target_dir))

            self.assertIn('Initializing new Python package', result)
            self.assertIn('Done!', result)

    @patch("sys.stdout", new_callable=StringIO)
    def test_list_plates(self, mock_stdout):
        args = {}
        command = cmd.ListPlates()
        command.execute(args)
        result = mock_stdout.getvalue()
        self.assertIn('python_package', result)
        self.assertIn('ansible_role', result)

    @patch("sys.stdout", new_callable=StringIO)
    def test_search_plates(self, mock_stdout):
        args = {'<phrase>': 'py'}
        command = cmd.SearchPlates()
        command.execute(args)
        result = mock_stdout.getvalue()
        self.assertIn('python_package', result)
        self.assertIn('python_script', result)
        self.assertNotIn('ansible_role', result)

    @patch("sys.stdout", new_callable=StringIO)
    def test_search_plates_not_found(self, mock_stdout):
        args = {'<phrase>': 'unfindable_package'}
        command = cmd.SearchPlates()
        command.execute(args)
        result = mock_stdout.getvalue()
        self.assertIn('No plates found.', result)
