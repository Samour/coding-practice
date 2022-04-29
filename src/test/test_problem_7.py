import unittest
from unittest.mock import patch
from io import StringIO
import re

from problem_7 import main


class WordsTestCase(unittest.TestCase):

  def _check_words(self, words, first, last):
    with patch('builtins.input', return_value=words), patch('sys.stdout', new=StringIO()) as output:
      main()
      output_text = output.getvalue()
      first_match = re.search('[Ff]irst [^\n]*{}\n'.format(first), output_text)
      last_match = re.search('[Ll]ast [^\n]*{}\n'.format(last), output_text)
      self.assertIsNotNone(first_match)
      self.assertIsNotNone(last_match)

  def test_colours(self):
    self._check_words('Black, Brown, Green, Red, Purple', 'Black', 'Purple')

  def test_weird_spacing(self):
    self._check_words('Melbourne ,Sydney,  Adelade, Hobart    ,Brisbane', 'Melbourne', 'Brisbane')

  def test_one_word(self):
    self._check_words('Singleton', 'Singleton', 'Singleton')

  def test_blanks(self):
    self._check_words(',Abc,', '', '')
  
  def test_no_words(self):
    self._check_words('', '', '')


if __name__ == '__main__':
  unittest.main()
