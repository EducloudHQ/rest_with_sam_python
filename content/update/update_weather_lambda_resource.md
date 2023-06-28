After inserting a weather item into the table, the next endpoint we'll create is 
`UpdateWeather`.

This endpoint would be used to update an existing weather item, with `id` of item as 
input.

In order to create this endpoint, we first have to define its resources under the `Resources` section of 
the `template.yaml` file and then define a `lambda_handler` in a src folder.

Type in the following code under resources in the `template.yaml` file.


```yaml

  UpdateWeather:
    Type: AWS::Serverless::Function
    Description: 'Lambda function updates weather item in DynamoDB table'
    Properties:
      FunctionName: UpdateWeatherLambda
      Handler: update_weather.lambda_handler

      Events:
        ApiEvent:
          Type: Api
          Properties:
            Path: /weather/{id}
            Method: PUT
            RestApiId: !Ref WeatherApi
    Connectors:
      updateWeatherItemToDB:
        Properties:
          Destination:
            Id: WeatherTable
          Permissions:
            - Write

```

`UpdateWeather` is the functions logical id.
`AWS::Serverless::Function` resource for a serverless function.

`Handler` refers to the location of the lambda_handler code, which we'll create in a minute.

`Events` refer to activities that trigger the lambda function.
In this case, when a `PUT` request is made to the endpoint at `Path` /weather/{id},
then this lambda function should be invoked.

Notice that the endpoint path parameter takes an id `/weather/{id}`.

This `id` corresponds to the id of the weather item to be updated.

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
            
  UpdateWeather:
    Type: AWS::Serverless::Function
    Description: 'Lambda function updates weather item in DynamoDB table'
    Properties:
      FunctionName: UpdateWeatherLambda
      Handler: update_weather.lambda_handler

      Events:
        ApiEvent:
          Type: Api
          Properties:
            Path: /weather/{id}
            Method: PUT
            RestApiId: !Ref WeatherApi
    Connectors:
      updateWeatherItemToDB:
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
  UpdateWeatherFunction:
    Description: "Update Weather Lambda Function ARN"
    Value: !GetAtt UpdateWeather.Arn
```

