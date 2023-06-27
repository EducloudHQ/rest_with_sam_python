We'll be storing the weather details in a dynamodb table.

Let's go ahead and create this table in the resources section of the `template.yaml` file.

Under `Resources` , type in the following yaml code

```yaml
Resources:

  WeatherTable:
    Type: AWS::DynamoDB::Table
    Properties:
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      ProvisionedThroughput:
        ReadCapacityUnits: 5
        WriteCapacityUnits: 5

```
 `WeatherTable` is the logical id of our dynamodb table. 
 `Type` is the resource type, which is `AWS::DynamoDB::Table`
 
Our table would have a primary key called id(`AttributeName`), which is a string as denoted by the `S` value 
in `AttributeType`.

A key schema specifies the attributes that make up the primary key of a table, or the key attributes of an index.

For our case, the attribute is `id` and the `KeyType` is `HASH` for primary key. Which is the role the attribute would assume.

We'll want to be able to access our dynamodb table name from all the other resources of our applications 
such as the lambda functions.

So let's add it to the `globals section`.

```yaml
# More info about Globals: https://github.com/awslabs/serverless-application-model/blob/master/docs/globals.rst
Globals:
  Function:
    Runtime: python3.10
    Timeout: 3
    MemorySize: 128
    Environment:
      Variables:
        TABLE_NAME: !Ref WeatherTable

```

With that added, let's go ahead and create our first lambda function.

