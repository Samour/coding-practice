import unittest
from unittest.mock import patch
from io import StringIO
import re
import math

from problem_3 import main


class AreaTestCase(unittest.TestCase):

  def _check_calculation(self, radius, expected_area):
    with patch('builtins.input', return_value=radius), patch('sys.stdout', new=StringIO()) as output:
      main()
      out_area = re.search(r'[0-9]+(\.[0-9]+)?', output.getvalue())
      
      self.assertIsNotNone(out_area)
      parsed_area = float(out_area[0])
      self.assertAlmostEquals(parsed_area, expected_area, delta=0.1)

  def _check_invalid(self, provided_input):
    with patch('builtins.input', return_value=provided_input), patch('sys.stdout', new=StringIO()) as output:
      main()
      out_area = re.match(r'[0-9]+(\.[0-9]+)?', output.getvalue())
      
      self.assertIsNone(out_area)

  def test_small_circle(self):
    self._check_calculation('1.26', 1.26 ** 2 * math.pi)

  def test_large_circle(self):
    self._check_calculation('678.91', 678.91 ** 2 * math.pi)

  def test_int_circle(self):
    self._check_calculation('502', 502 ** 2 * math.pi)

  def test_non_numeric(self):
    self._check_invalid('This is not a number')

  def test_mixed(self):
    self._check_invalid('12i.3')

  def test_blank(self):
    self._check_invalid('')


if __name__ == '__main__':
  unittest.main()
