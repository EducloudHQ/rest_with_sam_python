import json
import os

import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get("TABLE_NAME")
table = dynamodb.Table(table_name)


def lambda_handler(event, context):
    try:
        response = table.scan(TableName=table_name)
        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'])
        }
    except table_name:
        return {
            'statusCode': 500,
            'message': json.dumps({"message": "Unable to get weather"})
        }
