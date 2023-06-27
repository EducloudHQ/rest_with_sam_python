## Creating a SAM Project
1. To initialize a new SAM application,from your command line, type `sam init` command.

![alt text](https://raw.githubusercontent.com/EducloudHQ/rest_with_sam_python/master/assets/sam_init.png)

Enter `1` to select `AWS Quick Start Template` and hit enter to proceed.

![alt text](https://raw.githubusercontent.com/EducloudHQ/rest_with_sam_python/master/assets/sam_init_1.png)

We want to initialize a hello world application. So enter `1` and proceed.

![alt text](https://raw.githubusercontent.com/EducloudHQ/rest_with_sam_python/master/assets/sam_init_3.png)

We'll be using `python` as our runtime. So enter `Y` and proceed.

Follow the prompts as shown in the image below and proceed.

![alt text](https://raw.githubusercontent.com/EducloudHQ/rest_with_sam_python/master/assets/sam_init_4.png)

For the project name, I used `rest_weather_api`. 

Feel free to use a name of your choice.

Here's how a successful output looks like. 

![alt text](https://raw.githubusercontent.com/EducloudHQ/rest_with_sam_python/master/assets/sam_init_5.png)

You should have this folder structure, once you open up the project in an IDE. I recommend Pycharm for its awesomeness.
```

rest_weather_api
├── event
    ├── events.json
├── hello_world
    ├── _init_.py
    ├── app.py
    ├── requirements.txt
├── test
├── __init__.py
├── samconfig.toml
├── README.md
└── template.yaml
```
