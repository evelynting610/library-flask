# Library API
Simple Flask API to retrieve information about book requests.

## Stack

This app has a postgresql db and a flask API.  Both run on docker.
All the Flask code lives in the library folder of this repo, and the meat of the api call definitions live in [this file](library/views.py).
The Flask app is initialized in the `create_app` method of [this file](library/__init__.py) in the library folder

## Steps to Run Locally

1. Install Docker through the Docker website
2. Once installed, run the docker program. You should see a small whale carrying cargo containers in your Mac menu bar
3. Change into this `library-flask` directory in your terminal
4. Issue `docker-compose up -d`
5. Wait for a minute or two while the db gets up and running.
6. Run `docker-compose exec web flask db upgrade` and then `docker-compose exec web flask seed`.  This will migrate the db and seed some fake data.  The data it seeds lives in [this file](library/commands.py)

## Testing

**Note**: I have used `requested_at` instead of `timestamp`, and `book_id` instead of `id` for the request responses to be more clear (since I have other fields in that model that these could be confused with if I had gone with the generic names).

The backend is hosted locally on port 5000 and you can access the API by hitting http://localhost:5000/api/[your_api_endpoint]
