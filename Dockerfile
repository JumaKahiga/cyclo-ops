FROM python:3.6-slim-buster
LABEL maintainer="kabirumwangi@gmail.com"

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean


# Install python packages
COPY ./devops/docker/requirements.txt /home/docker/requirements.txt
RUN  pip install --upgrade-strategy only-if-needed --no-cache-dir -r /home/docker/requirements.txt


COPY . /cyclops
WORKDIR /cyclops/


ENV PYTHONPATH $PYTHONPATH:/cyclops
ENV FLASK_APP cyclops.unicorn:app
ENV FLASK_RUN_PORT 5000
EXPOSE 5000


CMD [\
	"gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "--timeout", "60", \
	"--access-logformat", "%(h)s %(l)s %(t)s \"%(r)s\" %(s)s %(b)sB %(L)ss \"%(a)s\"", \
	"--access-logfile", "-", "cyclops.unicorn:app" \
	]
