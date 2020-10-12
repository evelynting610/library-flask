# Library API
Simple Flask API to retrieve information about book requests.

## Stack

This app has a postgresql db and a flask API.  Both run on docker.
All the Flask code lives in the library folder of this repo.
The Flask app is initialized in the `create_app` method of [this file](library/__init__.py) in the library folder

## Steps to Run Locally

1. Install Docker through the Docker website
2. Once installed, run the docker program. You should see a small whale carrying cargo containers in your Mac menu bar
3. Change into the `library-flask` directory in your terminal
4. Issue `docker-compose up -d`
5. Run all the commands in ./bin/init-local-db.  This will also seed some fake data.  The data it seeds lives in [this file](library/commands.py)

The backend is hosted locally on port 5000 and you can access the API by hitting http://localhost:5000/api/[your_api_endpoint]
