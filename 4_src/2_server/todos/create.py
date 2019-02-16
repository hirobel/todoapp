import json
import logging
import os
import time
import uuid

import boto3
dynamodb = boto3.resource('dynamodb')

def create(event, context):
    data = json.loads(event['body'])
    if 'title' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")
        return

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # item = {
    #     'id': str(uuid.uuid1()),
    #     'text': data['text'],
    #     "checked": False,
    #     'createdAt': timestamp,
    #     'updatedAt': timestamp,
    # }

    item = {
        'id': str(uuid.uuid1()),
        'title': data['title'],
        "content": data['content'],
        'due_date': data['due_date'],
        'status': data['status'],
    }

    table.put_item(Item=item)

    response = {
        "statusCode" : 200,
        "body" : json.dumps(item)
    }

    return response