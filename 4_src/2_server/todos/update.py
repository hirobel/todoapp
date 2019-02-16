import json
import logging
import os

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def update(event, context):
    data = json.loads(event['body'])
    if 'title' not in data or 'status' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the todo item.")
        return

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

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

    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response