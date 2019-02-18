import sys; sys.path.append('../todos')
from unittest import TestCase
from nose.tools import ok_, eq_
from delete import validateInput

class DeleteTestCase(TestCase):

    def testValidateInput1(self):
        data = { 
            "id": "Test Id"
        }
        required_keys = ['id']
        error = validateInput(data, required_keys=required_keys)
        eq_(error['isError'], False)
        eq_(error['code'], '')
        eq_(error['text'], '')