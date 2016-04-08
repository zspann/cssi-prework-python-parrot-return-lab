import sys
import unittest
# Note, for python 3, just do 'from io import StringIO'
from io import BytesIO as StringIO
from parrot import *


class TestParrot(unittest.TestCase):

    def test_parrot_no_args(self):
        """It prints and returning Squawk if no arguments are given"""
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            parrot()
            output = out.getvalue().strip()
            self.assertEqual(output, 'Squawk!')
            self.assertEqual(parrot(),'Squawk!')
        finally:
            sys.stdout = saved_stdout


    def test_parrot_with_args(self):
        """It prints and returns the phrase if phrase if given as an argument"""
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            return_value = parrot("hello")
            output = out.getvalue().strip()
            self.assertEqual(output, 'hello')
            self.assertEqual(return_value,'hello')
        finally:
            sys.stdout = saved_stdout



if __name__ == '__main__':
    unittest.main()

