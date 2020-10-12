FROM python:3.7

RUN pip install --user -q pip

COPY ./ /app
WORKDIR /app
RUN pip install -r requirements.txt

# By default config_type will be prod (for dockerhub), is set to "development" for local builds
ARG config_type=production
ENV APP_CONFIG_FILE=/app/config/${config_type}.py

EXPOSE 5000

ENV FLASK_APP=library
CMD gunicorn -b 0.0.0.0:5000 -w 4 library:app
