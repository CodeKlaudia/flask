FROM python:3.7-slim

#Copy local code to the container image
ENV APP_HOME /app
WORKDIR SAPP_HOME

COPY .  ./

# Install production dependencies
RUN pip install Flask gunicorn

#EXPOSE

CMD exec gunicorn --bind:8080 --workers 1 --threads 1 app:app
