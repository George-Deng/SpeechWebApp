# BuddyGuy AI

## Front-end
The frontend aspect of this project is contained in the `/frontend` directory. Inside the directory there are a number of folders that contain pages for the website, css for the website, and components that each pages uses. The frontend is mainly used to take inputs or display outputs that are taken or received from the backend server. 

In order to Run the site locally you have cd into the frontend directory before you can call `npm start`

# Install NodeJS

This project requires you to have NodeJS installed

# Getting Started with Create React App (https://nodejs.org/en/) LTS version 

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

if there are issues with running `npm start` calling `npm install` usually fixes them

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)

## Back-end
The backend API is in the `/backend` directory. Inside of the directory, there are a number of files and folders that follow the MVC architecture recommended by [Django's project structure skeleton document.](https://django-project-skeleton.readthedocs.io/en/latest/structure.html) Within the folder is also a duplicate of certain functions found in the AI folder to integrate model inferencing online.

The backend API uses Django and Django rest framework. Django is a popular backend framework that uses the Model-View-Controller model to create web and mobile compatible backends. The project uses Django to process all the logic in the app interactions ranging from login to model inference to annotating to uploading and retrieving audio files. Django’s REST API extension was used to implement the architecture standard described below.

Dependencies for the backend API are recorded in the requirements.txt file.

The framework follows the REST API implementation recommended by the Django Rest Framework documentation linked [here.](https://www.django-rest-framework.org/)


To run the backend one must have docker and docker-compose installed in their machine. To run the API backend on port 8000, simply run the line
```
docker-compose up --build -d
```
in the same context as the docker-compose.yml file. 

This will run a linux server with a version of python that contains all of our C and Python dependencies to run the project succesfully.

## Machine Learning

The machine learning/prediction aspect of this project is contained within the `/ai` directory. Inside that directory, there are 4 Python files for the 2 different models that were trained. The `_model.py` files read in .csv files from within the `/sample_audio` folder, and create models to predict either the gender or the presence of Parkinson's. It then saves the model to disk with a `.sav` extension. It saves the models to disk so the `_input.py` files can read models into their program and give a prediction based on an input of a URL of an audio file. The `_input.py` files contain a single function which takes in a URL and returns a prediction. That function is called on by the back-end. All 4 files can be run using the command (the `_input.py` files will do nothing as there is no main()):

```
python3 <file_name>
```

The `/sample_audio` directory contains the audio data for both machine learning models. `voice.csv` is used for the gender prediction model, `parkinsons_data.csv` is for the Parkinson's prediction model. The directory also contains 2 sample `.wav` files which can be used to test the prediction functions.

Gender data taken from `http://www.primaryobjects.com/2016/06/22/identifying-the-gender-of-a-voice-using-machine-learning/`
Parkinson's data taken from `https://archive.ics.uci.edu/ml/datasets/Parkinson+Speech+Dataset+with++Multiple+Types+of+Sound+Recordings`

