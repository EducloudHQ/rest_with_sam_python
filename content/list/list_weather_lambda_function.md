Inside the `src` folder, create a file called `get_weathers.py`.

Open up the `get_weathers.py` file and type in the following code.

```python
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

```
After importing all required dependencies, the only significant change here is the dynamodb `scan`
method which scans and reads all items from the database table.

Using the `scan` method on really large tables would greatly affect the performance of your application,
unless you are using pagination.

For this use case, we only have a couple of items in our table, so no pagination.

`response = table.scan(TableName=table_name)`

We then wrap the method in a `try-except` block and return a status and a message, based on the result.

## Github Repository

The complete code for this section is in the `get_delete` branch of the project's Github repository [here](https://github.com/EducloudHQ/rest_with_sam_python/tree/get_delete)


