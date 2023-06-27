To be highly effective with the SAM IaC(Infrastructure as Code), it's essential to learn the basic
building blocks on a Sam template. 

AWS SAM is a high level abstraction of AWS CloudFormation, so when you build a SAM template, it compiles to 
cloudformation resources.

Here are the main sections of a SAM template file.

***Transform declaration***

This declaration identifies an AWS CloudFormation template file as an AWS SAM template file and it has 
the following declaration `Transform: AWS::Serverless-2016-10-31` which required for 
all SAM templates.

***Globals section***

This section is unique to AWS SAM and defines properties that are common to all your serverless functions and APIs.

We'll see how to use properties in this section to build our api effectively.

***Resources section***

In AWS SAM templates the Resources section can contain a combination of AWS CloudFormation resources and AWS SAM resources.

****Parameters section***

Objects that are declared in the Parameters section cause the sam deploy --guided command to present additional prompts to the user.

Let's proceed to create our api, functions and database by defining resources in the resources section 
of the SAM template file.
