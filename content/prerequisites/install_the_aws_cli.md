## Install the AWS CLI

We just created a new IAM user and got some credentials(AWS ACCESS KEY ID and SECRET).

Now, we have to install and configure the aws cli in order to work easily with aws services. 

Before we proceed, we must first install python3.3+. 

- [python installation](https://www.python.org/downloads/)
- [pip installation](https://pip.pypa.io/en/stable/installation/)

Now, refer to the official aws cli installation documentation [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)


## Configure AWS CLI with ACCESS KEY ID and SECRET

Open up your terminal and type the command

`aws configure`.

Copy and paste the Access Key Id and Secret when prompted.Choose your aws region. I choose `us-east-2`.

Then for output format, I choose `None`.

That's all.



