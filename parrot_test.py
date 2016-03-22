import sys
import unittest
from mock import patch
from io import StringIO
from parrot import *

class TestParrot(unittest.TestCase):

    def test_parrot_no_args(self):
        self.assertEqual(parrot(), "Squawk!")
        # with patch('sys.stdout', new=StringIO()) as fake_out:
        #     parrot()
        #     self.assertEqual(fake_out.getvalue(), "Squawk")
        # Need help figuring out how to test stdout...

    def test_parrot_with_args(self):
        self.assertEqual(parrot("hello"), "hello")
        self.assertEqual(parrot("hi Parrot"), "hi Parrot")



if __name__ == '__main__':
    unittest.main()


