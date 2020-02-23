FROM python:3.7-alpine3.11

# Copy local code to the container image.
ENV APP_HOME /app
ENV PORT 8080
ENV PYTHONPATH "${APP_HOME}/src"
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app