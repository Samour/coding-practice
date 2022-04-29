import unittest
from unittest.mock import patch
from io import StringIO
import re

from problem_6 import main


class ExtensionTestCase(unittest.TestCase):

  def _check_extension(self, filename, extension):
    with patch('builtins.input', return_value=filename), patch('sys.stdout', new=StringIO()) as output:
      main()
      match = re.match('(.* )?{}\n'.format(extension), output.getvalue())
      self.assertIsNotNone(match)

  def _check_blank(self, filename):
    with patch('builtins.input', return_value=filename), patch('sys.stdout', new=StringIO()) as output:
      main()
      match = re.match('(.*:)? ?\n', output.getvalue())
      self.assertIsNotNone(match)

  def test_docx(self):
    self._check_extension('some_file.docx', 'docx')

  def test_bin(self):
    self._check_extension('my_exec.bin', 'bin')

  def test_with_periods(self):
    self._check_extension('this.is.my.file', 'file')

  def test_with_spaces(self):
    self._check_extension('Some File.pdf', 'pdf')

  def test_no_extension(self):
    self._check_blank('logs')

  def test_spaces_no_extension(self):
    self._check_blank('Some Other File')

  def test_blank_extension(self):
    self._check_blank('file.')

  def test_blank_input(self):
    with patch('builtins.input', return_value=''), patch('sys.stdout', new=StringIO()):
      main()


if __name__ == '__main__':
  unittest.main()
