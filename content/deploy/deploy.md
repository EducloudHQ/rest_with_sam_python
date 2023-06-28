In order to test our api, we first need to deploy it to the cloud. 

SAM has the possibility of letting us deploy and test the application locally, with docker.

But it's preferable we use the cloud, since it's much suitable for this tutorial.

## Github Repository

You can get the complete code from [here](https://github.com/EducloudHQ/rest_with_sam_python/tree/master)

Once you have the complete code, open up your commandline interface and run the following commands.

```bash
sam build
sam deploy --guided
```

For the prompts and answers, here's what I inputted

Stack Name [rest_weather_api]: rest-weather-api   
AWS Region [us-east-2]: Press Enter key
Confirm changes before deploy [y/N]: y
Allow SAM CLI IAM role creation [Y/n]: Y
HelloWorldFunction may not have authorization defined, Is this okay? [y/N]: y
Save arguments to configuration file [Y/n]: Y
SAM configuration file [samconfig.toml]: Press Enter key
SAM configuration environment [default]: Press Enter key
Previewing CloudFormation changeset before deployment:

Deploy this changeset? [y/N]: y

You can find your API Gateway Endpoint URL in the output values displayed after deployment.

Once you get the API Gateway Endpoint URL, proceed to the next phase which is testing.