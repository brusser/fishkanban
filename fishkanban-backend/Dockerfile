FROM python:3
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

# Uncomment the following line to use NODB
# NODB will use SQLite and in-memory cache insstead of Postgres
# This is useful to test the rest of the Django setup without configuring the database/cache
# Comment it out and rebuild this image once you have Postgres and Redis services in your cluster
ENV NODB 1

# Install dependencies.
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Add application code.
WORKDIR /app
ADD . /app


# CMD export DJANGO_PASSWORD=$(cat /etc/secrets/djangouserpw); gunicorn -b :$PORT mysite.wsgi
CMD daphne -p 8000 fishkanban.asgi:application