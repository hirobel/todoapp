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

def list(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    result = table.scan()

    body = {
        'Result': 'success',
        'Errors': [],
        'Data': {}
    }
    body['Data'] =result['Items']
    response = {
        "statusCode": 200,
        "body": json.dumps(body,
                            cls=DecimalEncoder)
    }

    return response