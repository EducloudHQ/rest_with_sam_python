After creating the `WeatherTable`, let's create the `CreateWeatherFunction` lambda 
which adds weather items to the table.

First, we need to create the lambda function resource in `template.yaml` under resources.

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