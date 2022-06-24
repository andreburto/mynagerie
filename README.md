# Mynagerie

## About

Converting [my toy list](https://docs.google.com/spreadsheets/d/1Zyjqlez0W6x_9fOgcdDzoBx3W5gqzoX6fpInWkTjj8s/edit?usp=sharing) into an app.

## Requirements

#### Python

Python requirements are kept in the `requirements.txt` file within the project root directory.
These will mostly be installed during the image build stage using the Dockerfile.

#### JavaScript

The public facing UI uses [jQuery 3.6.0](https://blog.jquery.com/2021/03/02/jquery-3-6-0-released/) which needs to be manually installed.
This minified file is used.
Download the file and save it in `/src/mynagerie/static/js` as `jquery-3.6.0.min.js`.
It will be moved to the right place when `collectstatic` is run.


## To Do

* Toy list
* Toy dashboard

## Update Log

**2022-06-23:** Updated requirements section of README.
Started working on the JS part of the interface.

**2022-05-27:** Started working on JSON endpoints for the dashboard.
Created `start.bat` to speed up getting into the container when working on Windows.

**2022-05-21:** Added Wave model and added it to Toy model.

**2022-05-20:** Started the project.
Learned about dos2unix after wasting a lot of time.
Created the base Docker image.
Setup the database models and admin pages for them.
Stubbed in views.
