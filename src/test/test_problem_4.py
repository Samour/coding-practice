import unittest
from unittest.mock import patch
from io import StringIO

from problem_4 import main


class NameTestCase(unittest.TestCase):

  def _check_output(self, first_name, second_name):
    with patch('builtins.input', side_effect=[first_name, second_name]), patch('sys.stdout', new=StringIO()) as output:
      main()
      self.assertIn('{} {}'.format(second_name, first_name), output.getvalue())

  def test_name(self):
    self._check_output('firstname', 'secondname')

  def test_another_name(self):
    self._check_output('John', 'Smith')

  def test_with_spaces(self):
    self._check_output('This has', 'spaces')


if __name__ == '__main__':
  unittest.main()
