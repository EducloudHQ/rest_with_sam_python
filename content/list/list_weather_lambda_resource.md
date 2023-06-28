The last endpoint we are going to create would help us retrieve all weather items from 
the dynamodb table.
`GetAllWeather` lambda endpoint would help us get all weather items from the dynamodb table.

Type in the following code under Resources in the `template.yaml` file.

```yaml
  GetAllWeather:
    Type: AWS::Serverless::Function
    Description: 'Lambda function gets all weather item in DynamoDB table'
    Properties:
      FunctionName: GetsAllWeatherLambda
      Handler: get_weathers.lambda_handler

      Events:
        ApiEvent:
          Type: Api
          Properties:
            Path: /weathers
            Method: GET
            RestApiId: !Ref WeatherApi
    Connectors:
      getsWeatherItemToDB:
        Properties:
          Destination:
            Id: WeatherTable
          Permissions:
            - Read
```


`GetAllWeather` is the functions logical id.
`AWS::Serverless::Function` resource for a serverless function.

`Handler` refers to the location of the lambda_handler code, which we'll create in a minute.

`Events` refer to activities that trigger the lambda function.
In this case, when a `GET` request is made to the endpoint at `Path` /weathers, this lambda function should be invoked.

We assign a `Read` permission because we are reading data from the dynamoDB.

```yaml
    Connectors:
      getsWeatherItemToDB:
        Properties:
          Destination:
            Id: WeatherTable
          Permissions:
            - Read
```
Let's create the get all weather item lambda_handler now.