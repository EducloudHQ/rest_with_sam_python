## What is the AWS Serverless Application Model (SAM)
The AWS Serverless Application Model (SAM)  is an open-source  framework for building serverless applications. It provides shorthand syntax to express functions, APIs, databases, and event source mappings. With just a few lines per resource, you can define the application you want and model it using YAML. During deployment, SAM transforms and expands the SAM syntax into AWS CloudFormation syntax, enabling you to build serverless applications faster.

To get started with building SAM-based applications, one has to use the AWS SAM CLI . SAM CLI provides a Lambda-like execution environment that lets you locally build, test, and debug applications by defining SAM templates or through the AWS Cloud Development Kit (CDK). You can also use the SAM CLI to deploy your applications to AWS, or create secure continuous integration and deployment (CI/CD) pipelines that follow best practices and integrate with AWS' native and third party CI/CD systems.

SAM and SAM CLI are open-sourced under the Apache 2.0 license. You can contribute new features and enhancements to SAM on GitHub  or SAM CLI on GitHub .

## How does it work
AWS SAM provides shorthand syntax to express functions, APIs, databases, and event source mappings. During deployment, SAM transforms and expands the SAM syntax into AWS CloudFormation syntax. Afterward CloudFormation provisions your resources with reliable deployment capabilities.

## What is a SAM template?
A SAM template file is a YAML configuration that represents the architecture of a serverless application. You use the template to declare all the AWS resources that comprise your serverless application in one place. AWS SAM templates are an extension of AWS CloudFormation templates, so any resource that you can declare in an AWS CloudFormation template you can also declared in an AWS SAM template.

## How much does AWS SAM Cost to use?
There is no additional charge to use AWS SAM. You pay for the AWS resources created using SAM in the same manner as if you created them manually on an AWS Console. You only pay for the AWS resources that you use. There are no minimum fees and no required upfront commitments.

## How do I install the AWS SAM CLI?
You can install AWS SAM CLI on Linux, Mac, or Windows using pip. To get started, visit the [installation documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) .