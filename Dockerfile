FROM python:3.7.3-stretch

WORKDIR /FishingApp

ADD . /FishingApp

RUN pip install -r requirements.text

#run the command to start uWSGI
CMD ["uwsgi", "app.ini"]
