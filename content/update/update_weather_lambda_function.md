After creating the update weather lambda resource, lets proceed to create it's corresponding lambda function.

Inside the `src` folder, create a file called `update_weather.py`.

Open up the `update_weather.py` file and type in the following code.


```python

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




```
Let's break down everything that's happening in the above code.

Firstly, we import a `boto3`, which is the official python software development kit for AWS. 
We'll be using `boto3` to access all aws resources
`import boto3`.

Next, we get the dynamodb resource from boto3, import the `TABLE_NAME` environment variable we defined in 
the Global Section of the `template.yaml` file and then initialized our table.

```python 
dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get("TABLE_NAME")
table = dynamodb.Table(table_name)
```
In order to update a weather item in the database table, we need to pass in a pathParameter called `id`, alongside
the weather attributes we intend on updating.

We use the `json.loads()` method to get the values from the event body and path parameter.

```python

 weather = json.loads(event['body'])['weather']
    town = json.loads(event['body'])['town']
    print(f"event {event}")
    print(f"pathParameters {event['pathParameters']}")
    print(f"weather {weather}")
    print(f"town {town}")
    weather_id = event['pathParameters']['id']

```
We use a couple of print statements for logging.

There are much better ways to log and monitor events in our serverless applications. We'll be looking into those in 
other courses.

Next, we use the `update_item` dynamodb function to update the specific record. 

Bear in mind that this method edits an existing item’s attributes, or adds a new item to the table if it does not already exist.

You can put, delete, or add attribute values. You can also perform a conditional update on an existing item (insert a new attribute name-value pair if it doesn’t exist, or replace an existing name-value pair if it has certain expected attribute values)

You can also return the item’s attribute values in the same UpdateItem operation using the ReturnValues parameter.

We'll pass in a `Key` object which corresponds to the primary key of the item.

We'll set the `UpdateExpression` value to update both the weather and town attributes `"set #weather = :weather, #town = :town"` and 
return all new values by setting `ReturnValues="UPDATED_NEW"`



```python
table.update_item(
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
```


## Github Repository

The complete code for this section is in the `update` branch of the project's github repository [here](https://github.com/EducloudHQ/rest_with_sam_python/tree/update)
