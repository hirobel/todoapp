import json
import os
import boto3
import decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

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
    if data.get('status')!='New' and data.get('status')!='WIP' and data.get('status')!='Done' and data.get('status')!='Pending':
        error['code'] = 1002
        error['text'] = 'status value is invalid'
        error['isError'] = True
    return error

def update(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    data = json.loads(event['body'])
    data.update(id=event['pathParameters']['id'])
    error = validateInput(data, required_keys=['id','title', 'content', 'due_date', 'status'])

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
        body = {
            'Result': 'success',
            'Errors': [],
            'Data': {}
        }
        result = table.update_item(
            Key = {
                'id': event['pathParameters']['id']
            },
            ExpressionAttributeNames={
                '#todo_title': 'title',
                '#todo_status': 'status',
            },
            ExpressionAttributeValues={
                ':title': data['title'],
                ':content': data['content'],
                ':status': data['status'],
                ':due_date': data['due_date'],
            },
            UpdateExpression='SET #todo_title = :title, '
                             ' #todo_status = :status, '
                             'content = :content, '
                             'due_date = :due_date',
            ReturnValues='UPDATED_NEW'
        )
        body['Data'] = result['Attributes']
        response = {
            "statusCode": 200,
            "body": json.dumps(body,
                               cls=DecimalEncoder)
        }
        return response