Inside the `src` folder, create a file called `get_weather.py`.

Open up the `get_weather.py` file and type in the following code.

```python
import json
import os

import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get("TABLE_NAME")

table = dynamodb.Table(table_name)
def lambda_handler(event, context):
    weather_id = event['pathParameters']['id']
    try:
        response = table.get_item(Key={'id': weather_id})
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
        }
    except table_name:
        return {
            'statusCode': 500,
            'body': json.dumps('Error getting weather')
        }
```
In the above code, we import dynamodb resource from boto3 then use that to access our dynamodb table.

The weather item id is gotten from pathParameters event object and used as a value in 
getting an item from dynamodb.

`response = table.get_item(Key={'id': weather_id})`

We then wrap the method in a `try-except` block and return a status and a message, based on the result.


Firstly, we import a couple of libraries, but the highlight here is 
`import boto3`.

`boto3` is the official python software development kit for AWS. We'll be using `boto3`
to access all aws resources.

Next, we get the dynamodb resource from boto3, import the `TABLE_NAME` environment variable we defined in 
the Global Section of the `template.yaml` file and then initialized our table.

```python 
dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get("TABLE_NAME")
table = dynamodb.Table(table_name)
```
In order to add or insert a weather item to the database table, our lambda function expects the event body
to contain `weather` and `town` values.

We use the `json.loads()` method to get the above values from the event body like so.

```python

 weather = json.loads(event['body'])['weather']
 town = json.loads(event['body'])['town']

```
Remember we specified `id` as the primary key for the table. When inserting data 
into the table, we must have an `id` key value pair.

This `id` value must be unique for each item. For this case, generate a random number and assign to the id.

```python

 id = str(random.randrange(100, 999))
    item = {

        'id': id,
        'weather': weather,
        'town': town

    }
```
Finally, inside a `try` `except` block, we put the item into the table,
using `put_item` method.

```python
table.put_item(Item=item)
```
Then we return messages and appropriate status codes, depending on the success or failure of the 
process.

## Github Repository

The complete code for this section is in the `create` branch of the project's github repository [here](https://github.com/EducloudHQ/rest_with_sam_python/tree/create)
