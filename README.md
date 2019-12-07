# Is it lunchtime yet?

Find out using this app!

## Run locally

- `pipenv install`

- `FLASK_APP=app/app.py FLASK_ENV=development pipenv run flask run`

### Run tests

- `pipenv run python app/tests.py`

## Run with docker

- `cp docker-compose.example.yml docker-compose.yml`
- Change config in `docker-compose.yml`
- `docker-compose up`
OR
- Run defaults: `docker-compose -f docker-compose.example.yml up`
