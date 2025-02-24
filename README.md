# Sam Bowditch - Web-Developer Test 

*Introduction*
**Thank you for taking the time to review this test.**

I will begin by setting out a list of steps I took to approach this task, setting out my thought process as clearly and comprenhensively as I can.

I was unable to completely finish the project in the alloted time, as I was unable to properly connect the frontend portions with the backend. 

Throughout the test, I tried to implement test-driven development and was able to do so for the data importation and backend endpoint development. When I began developing the frontend portion, I found myself running out of time, and as I am not too familiar with Vue.js and Flask, I was running in the various bugs which experience would eliminate. 

I am extremely grateful for the opportunity to carry out this task, as it has been a fantastic learning experience for me. 

## HOW TO SET UP THE PROJECT

**Linux**

To install dependencies for the frontend portion, run the following in the frontend/deeper-fe directory

```bash
npm run install
```

To install dependencies for the backend portion, navigate back to the root of the project and run the following: 

```bash
python -m venv venv
source venv/bin/activate
pip install
```

To install dependencies for the import portion of the project, navigate to the import directory and run the following:

```bash
python -m venv venv
source venv/bin/activate
pip install
```

## Steps


### Set out project structure

+ The first thing I did was set up a MongoDB instance on my local machine. I downloaded the official Mongo Docker image and ran the container. 

+ My project root is the Test/ directory. I initialised a Git repo for this directory.

+ I added three sub-directories to manage the project:
    - backend/
    - frontend/
    - import_data/

    I initially thought that dockerising the project would be the best approach, and indeed it could be useful for similar projects. Because of the mixture and independence of the frontend and backend portions of the project, I could use docker compose to initialise both subdirectories with respective dependencies.

    I also wanted to separate the backend code from the import code, as they deal with different aspects of the project. This being said, I could make adjustments to centralising the models and utility functions in one place.

### Testing Strategy
    
I tried to implement a test-based approach to building up the project as much as possible. Naturally, I implemented different testing strategies for both the frontend and backend portions of the project

+ *import_data*
    - I devised a test suite to see whether I had a valid connection to the MongoDB server, and whether the data from the json file had the correct shape.
    - I separated the testing databases from the "production" version.
    - To run the test suite, navigate to import_data/ directory, and activate the Python venv there. Then run pytest.
    - You will need to configure the MONGODB_SETTINGS in the conftest.py file to ensure you have a connection to a live MongoDB  server instance.

+ *Backend*
    - I need to mock a Flask app instance and send dummy data to the applicaiton in the test. To do so I reviewd the testing guidelines provided in the Flask documentation.
    - I created a tests/ subdirectory in the backend folder to contain my test code.
    - There, I tested the create, update, deleted, read methods. 
    - To run the test suite, navigate to backend/ directory, and activate the Python venv there. Then run pytest.
    - You will need to configure the MONGODB_SETTINGS in the conftest.py file to ensure you have a connection to a live MongoDB  server instance.

+ *Frontend*
    - I was unable to write any tests for the frontend portion of the task, however I had considered a strategy to do. In particular I was considering using jest to mock fetch requests to the local server, and then run assertion tests on what is rendered on the screen given a response. 


### Open API Specifcation

+ As part of the planning stage, I wrote an OpenAPI Specification in the backend/ directory to help me keep track of the shape of the API.

### Running the project

+ Before beginning, you will need to run the data import code. You will need to configure the .env file located under import_data/src and backend/f_app directories to ensure you are connected to a server.

+ Then to import the data, navigate up to the import_data/src directory, and run python import_data.py

+ After the import is successful, navigate into the frontend/deeper-fe/ directory to land in the frontend development area. Then to build the project, run npm run build. This will output the static build files to the backend/static/ directory.

+ To run the Flask server and server the frontend code, navigate to the backend/ directory, enter the python venv there, and run flask --app f_app run. This will start an instance of the flask server and will be accessible on 127.0.0.1:5000 in your browser. 


## Summary

+ I realised that I spent a lot of time debugging issues which I have not had much experience with in the recent past, such as API development and frontend - backend communication. With that said, I am extremely happy to have taken part in the task and I am motivated to continue building on my fullstack development skills.


