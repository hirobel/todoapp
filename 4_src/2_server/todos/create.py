import json
import os
import uuid
import boto3

def validateInput(data, required_keys=[]):
    error = {
        'isError':False,
        'code': '',
        'text': '',
    }
    for k in required_keys:
        if k not in data:
            error['code'] = 1000
            error['text'] = 'Required parameter does not exist'
            error['isError'] = True
        elif not data[k]:
            error['code'] = 1001
            error['text'] = 'Required parameter value is invalid'
            error['isError'] = True
    return error


def create(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    data = json.loads(event['body'])

    error = validateInput(data, required_keys=['title', 'content', 'due_date', 'status'])
    if error['isError']:
        body = {
            'Result': 'failed',
            'Errors': []
        }
        body['Errors'] = error
        response = {
            "statusCode" : 400,
            "body" : json.dumps(body),
        }
        return response
    else:
        item = {
            'id': str(uuid.uuid1()),
            'title': data['title'],
            "content": data['content'],
            'due_date': data['due_date'],
            'status': data['status'],
        }
        body = {
            'Result': 'success',
            'Errors': [],
            'Data': {}
        }
        body['Data'] = item
        table.put_item(Item=item)
        response = {
            "statusCode" : 200,
            "body" : json.dumps(body)
        }
        return response