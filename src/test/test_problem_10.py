import unittest
from unittest.mock import patch
from io import StringIO

from problem_10 import main


class RewordTestCase(unittest.TestCase):

  def _check_output(self, initial_sentence, expect_output):
    with patch('builtins.input', return_value=initial_sentence), patch('sys.stdout', new=StringIO()) as output:
      main()

      self.assertEqual(expect_output, output.getvalue().strip())

  def test_sentence(self):
    self._check_output('This is a sentence', 'Is This is a sentence')

  def test_another_sentence(self):
    self._check_output('This is another sentence', 'Is This is another sentence')

  def test_starts_with_is(self):
    self._check_output('Is this a sentence', 'Is this a sentence')

  def test_starts_lowercase_is(self):
    self._check_output('is this lowercase', 'is this lowercase')

  def test_starts_shouting_is(self):
    self._check_output('IS THIS TOO LOUD', 'IS THIS TOO LOUD')

  def test_confusing_start(self):
    self._check_output('issues with this one?', 'issues with this one?')


if __name__ == '__main__':
  unittest.main()
