import unittest
from unittest.mock import patch
from io import StringIO

from problem_9 import main


class CloseToTestCase(unittest.TestCase):

  def _check_close(self, value, expect_result):
    with patch('builtins.input', return_value=value), patch('sys.stdout', new=StringIO()) as output:
      main()
      find_token = 'Yes' if expect_result else 'No'
      self.assertIn(find_token, output.getvalue())

  def _check_invalid(self, value):
    with patch('builtins.input', return_value=value), patch('sys.stdout', new=StringIO()):
      main()

  def test_thousand_lower_bound(self):
    self._check_close('900', True)

  def test_thousand_lower(self):
    self._check_close('980', True)

  def test_thousand_equal(self):
    self._check_close('1000', True)

  def test_thousand_higher(self):
    self._check_close('1002', True)

  def test_thousand_upper_bound(self):
    self._check_close('1100', True)

  def test_two_thousand_lower_bound(self):
    self._check_close('1900', True)

  def test_two_thousand_lower(self):
    self._check_close('1940', True)

  def test_two_thousand_equal(self):
    self._check_close('2000', True)

  def test_two_thousand_higher(self):
    self._check_close('2031', True)

  def test_two_thousand_upper_bound(self):
    self._check_close('2100', True)

  def test_too_low(self):
    self._check_close('8', False)

  def test_in_between(self):
    self._check_close('1200', False)

  def test_too_high(self):
    self._check_close('3030', False)

  def test_fraction_close(self):
    self._check_close('920.39', True)

  def test_fraction_far(self):
    self._check_close('5382.81', False)

  def test_not_a_number(self):
    self._check_invalid('abc')

  def test_blank(self):
    self._check_invalid('')


if __name__ == '__main__':
  unittest.main()
