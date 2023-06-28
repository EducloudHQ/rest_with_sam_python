Inside the `src` folder, create a file called `delete_weather.py`.

Open up the `delete_weather.py` file and type in the following code.

```python
import json
import os

import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get("TABLE_NAME")

table = dynamodb.Table(table_name)


def lambda_handler(event, context):
    weather_id = event['pathParameters']['id']
    print(f"weather id {weather_id} is being deleted")

    try:
        table.delete_item(Key={
            "id": weather_id
        })
        return {
            'statusCode': 200,
            'body': json.dumps({"message": "Weather item deleted successfully"})
        }
    except table_name:
        return {
            'statusCode': 500,
            'body': json.dumps({"message": "Weather item not deleted successfully"})
        }

```
In the above code, we import dynamodb resource from boto3 then use that to access our dynamodb table.

The weather item id is gotten from pathParameters event object and used as a value in 
deleting an item from dynamodb.

`        table.delete_item(Key={
            "id": weather_id
        })`

We then wrap the method in a `try-except` block and return a status and a message, based on the result.


## Github Repository

The complete code for this section is in the `get_delete` branch of the project's Github repository [here](https://github.com/EducloudHQ/rest_with_sam_python/tree/get_delete)
