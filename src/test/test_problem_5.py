import unittest
from unittest.mock import patch
from io import StringIO

from problem_5 import main


class IterableTestCase(unittest.TestCase):

  def _check_output(self, values, expected_list):
    with patch('builtins.input', return_value=values), patch('sys.stdout', new=StringIO()) as output:
      main()

      printed = output.getvalue()
      self.assertIn('{}\n'.format(expected_list), printed)
      self.assertIn('{}'.format(tuple(expected_list)), printed)

  def _check_invalid(self, values):
    with patch('builtins.input', return_value=values), patch('sys.stdout', new=StringIO()) as output:
      main()

  def test_numbers(self):
    self._check_output('3,8,2,9,7', [3, 8, 2, 9, 7])

  def test_more_numbers(self):
    self._check_output('8, 33, 72, -1, 5, -80, 0', [8, 33, 72, -1, 5, -80, 0])

  def test_weird_spacing(self):
    self._check_output('30,    7,2,3   ,8', [30, 7, 2, 3, 8])

  def test_non_numeric(self):
    self._check_invalid('3, 9, a, 7')

  def test_missing_element(self):
    self._check_invalid('3, 9, 1,,2')

  def test_empty_input(self):
    self._check_invalid('')


if __name__ == '__main__':
  unittest.main()
