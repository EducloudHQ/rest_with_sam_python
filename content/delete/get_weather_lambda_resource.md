Let's write a lambda function resource to get a single item from the dynamodb table.

`GetWeather` lambda endpoint would help us get a weather item from the dynamodb table.

Type in the following code under Resources in the `template.yaml` file.

```yaml

   GetWeather:
    Type: AWS::Serverless::Function
    Description: 'Lambda function gets weather item in DynamoDB table'
    Properties:
      FunctionName: GetWeatherLambda
      Handler: get_weather.lambda_handler

      Events:
        ApiEvent:
          Type: Api
          Properties:
            Path: /weather/{id}
            Method: GET
            RestApiId: !Ref WeatherApi
    Connectors:
      getWeatherItemToDB:
        Properties:
          Destination:
            Id: WeatherTable
          Permissions:
            - Read
```


`GetWeather` is the functions logical id.
`AWS::Serverless::Function` resource for a serverless function.

`Handler` refers to the location of the lambda_handler code, which we'll create in a minute.

`Events` refer to activities that trigger the lambda function.
In this case, when a `GET` request is made to the endpoint at `Path` /weather/{id},
then this lambda function should be invoked.

This `id` corresponds to the id of the weather item we are getting.

When you specify a resource's logical name, it returns a value that you can typically use to refer to that resource.

You need permissions to access any resource in the cloud. 

Remember that the lambda function needs to get a weather item in dynamodb table. 

Therefore, we need to give the lambda function permission to do so.

We assign a `Read` permission because we are reading data to dynamoDB.

```yaml
    Connectors:
      getWeatherItemToDB:
        Properties:
          Destination:
            Id: WeatherTable
          Permissions:
            - Read
```
Let's create the lambda_handler now.