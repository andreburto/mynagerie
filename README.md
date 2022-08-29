# Mynagerie

## About

Converting [my toy list](https://docs.google.com/spreadsheets/d/1Zyjqlez0W6x_9fOgcdDzoBx3W5gqzoX6fpInWkTjj8s/edit?usp=sharing) into an app.

## Requirements

#### AWS

For the app and deployment scripts to work you will need AWS credentials that can manipulate Route53 and S3.
These credentials should be put in the `.env` file in the root of the project.
The variables names should be the default AWS ones for the access id and secret key.

#### Python

Python requirements are kept in the `requirements.txt` file within the project root directory.
These will mostly be installed during the image build stage using the Dockerfile.

#### JavaScript

The public facing UI uses [jQuery 3.6.0](https://blog.jquery.com/2021/03/02/jquery-3-6-0-released/) which needs to be manually installed.
This minified file is used.
Download the file and save it in `/src/mynagerie/static/js` as `jquery-3.6.0.min.js`.
It will be moved to the right place when `collectstatic` is run.

#### Terraform

[Terraform](https://www.terraform.io/) is used to create AWS resources that will be used by the app.

## To Do

* Toy dashboard should be interactive.
* App deployment instructions.
* Static site that can run from app or JSON.
* Mobile and desktop apps, for fun.
* Add generalized field comparator to allow multiple sources from Google Sheets.
* Tests, tests, tests.

## Update Log

**2022-08-28:** Moved Google tables out of `toys` app and into `auth_tools`.
Deleted old tables and manually migrated data to the new ones, so no complex migration files.
Need to make tests if I'm going to start moving tables around.

**2022-07-31:** Fixed start scripts to use `--rm` to clean up containers.
Fixed `start.bat` to run from project root directory and project `bin` directory.

**2022-07-13:** Started working on adding a Lambda function for a cloud-based endpoint.
Created the `load-envfile.ps1` script to load environment variables from a Docker-based file while in PowerShell.
This is needed for Terraform to work.

**2022-07-04:** Added the ability to compare the local toy list with the primary source on Google Sheets.
Can now store Google credentials and sheet ranges in the database.

**2022-07-03:** Made `start.sh` a script to run on *nix systems to match `start.bat` on Windows.
Updated `Dockerfile` to use `run.sh` when starting the app.
Added admin feature to publish toys JSON to S3.

**2022-07-02:** Added initial Terraform scripts.
Cleaned up the "start" scripts so they now automatically start the app.
**DID NOT** rewrite `start.bat` to be a PowerShell file despite my desire.
Created the initial JS display for toy lists.

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
