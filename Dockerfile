from python:3.7-alpine

WORKDIR /install
COPY Pipfile Pipfile.lock /install/
RUN pip install pipenv
# install packages system wide
RUN pipenv install --system

WORKDIR /app
COPY ./app/ /app/

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_ENVIRONMENT=prod

ENTRYPOINT ["flask", "run"]
