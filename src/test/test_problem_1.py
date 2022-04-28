import unittest
from unittest.mock import patch
from io import StringIO

from problem_1 import main


EXPECTED_OUTPUT = """Twinkle, twinkle, little star,
\tHow I wonder what you are!
\t\tUp above the world so high,
\t\tLike a diamond in the sky.
Twinkle, twinkle, little star,
\tHow I wonder what you are"""


class TwinkleTestCase(unittest.TestCase):

  def test_output(self):
    with patch('sys.stdout', new=StringIO()) as output:
      main()
      self.assertEqual(output.getvalue().strip(), EXPECTED_OUTPUT)


if __name__ == '__main__':
  unittest.main()
