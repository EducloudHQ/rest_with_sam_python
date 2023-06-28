Next on the list of endpoints to be created is the delete weather endpoint.

This endpoint comes in handy, when we want to delete a weather item from the database.

Type in the following code under Resources in the `template.yaml` file.

```yaml
  DeleteWeather:
    Type: AWS::Serverless::Function
    Description: 'Lambda function deletes weather item from DynamoDB table'
    Properties:
      FunctionName: DeleteWeatherLambda
      Handler: delete_weather.lambda_handler

      Events:
        ApiEvent:
          Type: Api
          Properties:
            Path: /weather/{id}
            Method: DELETE
            RestApiId: !Ref WeatherApi
    Connectors:
      deleteWeatherItemToDB:
        Properties:
          Destination:
            Id: WeatherTable
          Permissions:
            - Write
```


`DeleteWeather` is the functions logical id.
`AWS::Serverless::Function` resource for a serverless function.

`Handler` refers to the location of the lambda_handler code, which we'll create in a minute.

`Events` refer to activities that trigger the lambda function.
In this case, when a `DELETE` request is made to the endpoint at `Path` /weather/{id},
this lambda function would be invoked.

`id` here corresponds to the id of the weather item we wish to delete.

Deleting an item from the dynamodb table is a write request. 

So we need to pass in write permissions to our lambda function.


```yaml
    Connectors:
      deleteWeatherItemToDB:
        Properties:
          Destination:
            Id: WeatherTable
          Permissions:
            - Write
```
Next up, we have to create the delete lambda function.