
# Build a serverless rest api with AWS SAM, Api Gateway and Python
This course would walk you through building CRUDL(Create, Read, Update, Delete, List) api for a weather application.

The application uses several AWS resources, including Lambda functions and an API Gateway API. 

For resource provisioning, we'll be using AWS SAM.

## Prerequisite
Before proceeding, please make sure you have these installed and configured properly.

1. [AWS Account](https://aws.amazon.com/):
We'll be deploying the application to the AWS Cloud in order to test and confirm its functionalities.

2. [AWS Command Line Interface (AWS CLI)](https://awscli.amazonaws.com/AWSCLIV2.msi). The AWS CLI provides direct access to the public APIs of AWS services. You can explore a service's capabilities with the AWS CLI, and develop shell scripts to manage your resources
3. [ AWS SAM CLI](https://github.com/aws/aws-sam-cli/releases/latest/download/AWS_SAM_CLI_64_PY3.msi). AWS Serverless Application Model Command Line Interface, provides a Lambda-like execution environment that lets you locally build, test, and debug applications defined by SAM templates or through the AWS Cloud Development Kit (CDK)
4. [Python](https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe). The programming language used in this project
5. [Postman](https://www.postman.com/downloads/). Postman is an API platform for building and using APIs. Postman simplifies each step of the API lifecycle and streamlines collaboration so you can create better APIs—faster.

We'll be using the Pycharm IDE alongside, the AWS Toolkit to build and test our api.

The AWS Toolkit is an open source plug-in for popular IDEs that uses the SAM CLI to build and deploy serverless applications on AWS. 

The AWS Toolkit also adds a simplified step-through debugging experience for Lambda function code. 

See the following links to get started.

* [PyCharm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)

* [VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html)
* [Visual Studio](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/welcome.html)

## AWS Services used
1. [AWS SAM ](https://aws.amazon.com/serverless/sam/) To define the infrastructure : The AWS Serverless Application Model (SAM) is an open-source framework for building serverless applications. It provides shorthand syntax to express functions, APIs, databases, and event source mappings. With just a few lines per resource, you can define the application you want and model it using YAML. There is no additional charge to use AWS SAM. You pay for the AWS resources created using SAM in the same manner as if you created them manually. You only pay for what you use, as you use it. There are no minimum fees and no required upfront commitments.
2. [Amazon Cognito](https://aws.amazon.com/cognito/): With Amazon Cognito, you can add user sign-up and sign-in features and control access to your web and mobile applications. This service is free for less than 50,000 MAUs(monthly active users).
3. [API GATEWAY](https://aws.amazon.com/api-gateway/):Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. With Amazon API Gateway, you only pay when your APIs are in use. There are no minimum fees or upfront commitments
4. [AWS Lambda](https://aws.amazon.com/lambda/) : AWS Lambda is a serverless, event-driven compute service that lets you run code for virtually any type of application or backend service without provisioning or managing servers. You can trigger Lambda from over 200 AWS services and software as a service (SaaS) applications, and only pay for what you use. Cost of using lambda functions.
 ![](img/lp.png)