After creating the `WeatherTable`, let's create the weather api resource
which adds methods that can be invoked through HTTPS endpoints.

In the `template.yaml` file, under `Resources`, add the following yaml code

```yaml
  WeatherApi:
    Type: AWS::Serverless::Api
    Properties:
      StageName: dev
      Description: serverless api for weather application

```
`WeatherApi` is the logical id for our api.
`AWS::Serverless::Api` is the type of api(Api gateway)

For properties, we have the `StageName` set to `dev` and `Description` of the api. 

This is enough for our simple api. If you need to enhance the api further, please 
check-out the complete api gateway properties [guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-api.html).

Here's how our `template.yaml` file looks like now.

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

```