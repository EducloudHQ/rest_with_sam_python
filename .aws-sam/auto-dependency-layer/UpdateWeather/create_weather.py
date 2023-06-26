import json
import os
import random

import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get("TABLE_NAME")
table = dynamodb.Table(table_name)



def lambda_handler(event, context):
    print(f"event is {event}")
    print(f"table name is {table_name}")
    weather = json.loads(event['body'])['weather']
    town = json.loads(event['body'])['town']
    id = str(random.randrange(100, 999))
    item = {

        'id': id,
        'weather': weather,
        'town': town

    }
    try:
        table.put_item(Item=item)
        return {
            'statusCode': 200,
            'body': json.dumps({"message":"Weather successfully created!"})
        }

    except  Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"message":str(e)})
        }
