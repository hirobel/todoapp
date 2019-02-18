import sys; sys.path.append('../todos')
from unittest import TestCase
from nose.tools import ok_, eq_
from create import validateInput

class CreateTestCase(TestCase):

    def testValidateInput1(self):
        data = { 
            "title": "Test Title",
            "content": "Test Content",
            "due_date": 1550288140777,
            "status": "New"
        }
        required_keys = ['title', 'content', 'due_date', 'status']
        error = validateInput(data, required_keys=required_keys)
        eq_(error['isError'], False)
        eq_(error['code'], '')
        eq_(error['text'], '')

    def testValidateInput2(self):
        data = { 
            "content": "Test Content",
            "due_date": 1550288140777,
            "status": "New"
        }
        required_keys = ['title', 'content', 'due_date', 'status']
        error = validateInput(data, required_keys=required_keys)
        eq_(error['isError'], True)
        eq_(error['code'], 1000)
        eq_(error['text'], 'Required parameter does not exist')

    def testValidateInput3(self):
        data = { 
            "title": "",
            "content": "Test Content",
            "due_date": 1550288140777,
            "status": "New"
        }
        required_keys = ['title', 'content', 'due_date', 'status']
        error = validateInput(data, required_keys=required_keys)
        eq_(error['isError'], True)
        eq_(error['code'], 1001)
        eq_(error['text'], 'Required parameter value is invalid')

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

    def testValidateInput2(self):
        data = {}
        required_keys = ['id']
        error = validateInput(data, required_keys=required_keys)
        eq_(error['isError'], True)
        eq_(error['code'], 1000)
        eq_(error['text'], 'Required parameter does not exist')                