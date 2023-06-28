Now that we've created the api gateway, let's jump right in and create our first endpoint. 

`CreateWeather` lambda endpoint would help us add weather items to the dynamo db table.

In order to create this endpoint, we first have to define it's resources under the `Resources` section of 
the `template.yaml` file and then define a `lambda_handler` in a src folder.

Type in the following code under resources in the `template.yaml` file.

```yaml

  CreateWeather:
    Type: AWS::Serverless::Function
    Description: 'Lambda function inserts weather data into DynamoDB table'
    Properties:
      FunctionName: CreateWeatherLambda
      Handler: create_weather.lambda_handler
      Events:
        ApiEvent:
          Type: Api
          Properties:
            Path: /create-weather
            Method: POST
            RestApiId: !Ref WeatherApi
    Connectors:
      addWeatherItemToDB:
        Properties:
          Destination:
            Id: WeatherTable
          Permissions:
            - Write

```


`CreateWeather` is the functions logical id.
`AWS::Serverless::Function` resource for a serverless function.

`Handler` refers to the location of the lambda_handler code, which we'll create in a minute.

`Events` refer to activities that trigger the lambda function.
In this case, when a `POST` request is made to the endpoint at `Path` /create-weather,
then this lambda function should be invoked.

`!Ref` is a cloudformation intrinsic function that returns the value of the specified parameter or resource.

When you specify a resource's logical name, it returns a value that you can typically use to refer to that resource.

In this case, we have `RestApiId: !Ref WeatherApi` which returns the value of the `WeatherApi`
resources and assigns that value to `RestApiId`.

Therefore this lambda function belongs to the rest api we created before.

You need permissions to access any resource in the cloud. 

There are different types of permissions and different types of entity access. 

Remember that the lambda function needs to add/save weather items in dynamodb table. 

Therefore, we need to give the lambda function permission to do so.

We'll use the newly added SAM connectors, to configure fine grain write permissions between 2 resources.The lambda function and 
dynamodb.

We assign a `Write` permission because we are writing(adding/saving) data to dynamoDB.

```yaml
    Connectors:
      addWeatherItemToDB:
        Properties:
          Destination:
            Id: WeatherTable
          Permissions:
            - Write
```

Here's the complete `template.yaml` file.

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: >
  rest_weather_api

  Sample SAM Template for rest_weather_api

# More info about Globals: https://github.com/awslabs/serverless-application-model/blob/master/docs/globals.rst
Globals:
  Function:
    Runtime: python3.10
    CodeUri: src/
    Timeout: 3
    MemorySize: 128
    Environment:
      Variables:
        TABLE_NAME: !Ref WeatherTable
Resources:
  WeatherApi:
    Type: AWS::Serverless::Api
    Properties:
      StageName: dev
      Description: serverless api for weather application


  CreateWeather:
    Type: AWS::Serverless::Function
    Description: 'Lambda function inserts weather data into DynamoDB table'
    Properties:
      FunctionName: CreateWeatherLambda
      Handler: create_weather.lambda_handler
      Events:
        ApiEvent:
          Type: Api
          Properties:
            Path: /create-weather
            Method: POST
            RestApiId: !Ref WeatherApi
    Connectors:
      addWeatherItemToDB:
        Properties:
          Destination:
            Id: WeatherTable
          Permissions:
            - Write
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

Outputs:
  # ServerlessRestApi is an implicit API created out of Events key under Serverless::Function
  # Find out more about other implicit resources you can reference within SAM
  # https://github.com/awslabs/serverless-application-model/blob/master/docs/internals/generated_resources.rst#api
  WeatherApi:
    Description: "API Gateway endpoint URL for dev stage for create weather function"
    Value: !Sub "https://${WeatherApi}.execute-api.${AWS::Region}.amazonaws.com/dev/"
  CreateWeatherFunction:
    Description: "Create Weather Lambda Function ARN"
    Value: !GetAtt CreateWeather.Arn
```

