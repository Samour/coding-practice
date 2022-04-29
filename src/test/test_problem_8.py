import unittest
from unittest.mock import patch
from io import StringIO

from problem_8 import main


class TripleSumTestCase(unittest.TestCase):

  def _check_output(self, number, expect_result):
    with patch('builtins.input', return_value=number), patch('sys.stdout', new=StringIO()) as output:
      main()
      self.assertIn(expect_result, output.getvalue())

  def _check_invalid(self, number):
    with patch('builtins.input', return_value=number), patch('sys.stdout', new=StringIO()):
      main()

  def test_value(self):
    self._check_output('3', '369')
  
  def test_another_value(self):
    self._check_output('8', '984')

  def test_zero(self):
    self._check_output('0', '0')

  def test_multi_digit(self):
    self._check_invalid('32')

  def test_negative(self):
    self._check_invalid('-3')

  def test_non_numeric(self):
    self._check_invalid('a')

  def test_blank(self):
    self._check_invalid('')


if __name__ == '__main__':
  unittest.main()
