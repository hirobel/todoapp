import sys; sys.path.append('../todos')
from unittest import TestCase
from nose.tools import ok_, eq_
from update import validateInput

class UpdateTestCase(TestCase):

    def testValidateInput1(self):
        data = { 
            "id": "Test Id",
            "title": "Test Title Modified",
            "content": "Test Content",
            "due_date": 1550288140777,
            "status": "New"
        }
        required_keys = ['id']
        error = validateInput(data, required_keys=required_keys)
        eq_(error['isError'], False)
        eq_(error['code'], '')
        eq_(error['text'], '')

    def testValidateInput2(self):
        data = { 
            "title": "Test Title Modified",
            "content": "Test Content",
            "due_date": 1550288140777,
            "status": "New"
        }
        required_keys = ['id']
        error = validateInput(data, required_keys=required_keys)
        eq_(error['isError'], True)
        eq_(error['code'], 1000)
        eq_(error['text'], 'Required parameter does not exist')