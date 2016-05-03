FROM python:3.5.1

RUN apt-get update && \
    apt-get -y install postgresql-client libpq-dev --no-install-recommends

RUN mkdir /code
COPY . /code/
RUN cd /code/ && pip install -r requirements.txt
WORKDIR /code/elwrapper/
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "elwrapper.wsgi"]
