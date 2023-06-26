import json
import os

import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get("TABLE_NAME")
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    weather = json.loads(event['body'])['weather']
    town = json.loads(event['body'])['town']
    print(f"event {event}")
    print(f"pathParameters {event['pathParameters']}")
    print(f"weather {weather}")
    print(f"town {town}")
    weather_id = event['pathParameters']['id']
    print(f"weather_id {weather_id}")

    try:
        response = table.update_item(
            Key={
                'id': weather_id
            },
            UpdateExpression="set #weather = :weather, #town = :town",
            ExpressionAttributeNames={
                "#weather": "weather",
                "#town": "town"
            },
            ExpressionAttributeValues={
                ":weather": weather,
                ":town": town
            },
            ReturnValues="UPDATED_NEW"
        )
        return {
            'statusCode': 200,
            'body': json.dumps(response['Attributes'])
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Something went wrong'})
        }



