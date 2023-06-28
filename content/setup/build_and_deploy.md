## Build and deploy SAM Project

Before proceeding, it's essential we build and deploy our hello world application, to ensure everything's
working well from the start.

Execute the following commands to build and deploy the SAM project.

```
sam build

sam deploy --guided
```

The `sam build` command will build the source of your application. 

The SAM CLI installs dependencies defined in `hello_world/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

The `sam deploy --guided` command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.


Stack Name [rest_weather_api]: rest-weather-api    -->` Never use underscores for a stack name`
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
