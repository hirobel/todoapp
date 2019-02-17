import sys; sys.path.append('../todos')
from unittest import TestCase
from nose.tools import ok_, eq_
from create import validateInput

class HogeTestCase(TestCase):

    def testValidateInput1(self):
        data = {'a':1, 'b':2} 
        required_keys = ['a', 'b']
        error = validateInput(data, required_keys=required_keys)
        eq_(error['isError'], False)
        eq_(error['code'], '')
        eq_(error['text'], '')