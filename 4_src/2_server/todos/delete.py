import os
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

def delete(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    data = {
            'id': event['pathParameters']['id']
    }

    error = validateInput(data, required_keys=['id'])

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
        table.delete_item(
            Key={
                'id': event['pathParameters']['id']
            }
        )
        response = {
            "statusCode" : 204
        }
        return response
