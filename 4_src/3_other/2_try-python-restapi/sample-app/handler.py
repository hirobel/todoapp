import json


def infoRead(event, context):
    responseBody = {
        "result": "success",
        "data": [
            {
                "id": 1,
                "title": "",
                "content": "",
                "due-date": "",
                "status": ""
            }
        ]
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(responseBody)
    }

    return response