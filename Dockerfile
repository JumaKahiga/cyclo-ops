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

COPY ./devops/docker/entry_point.sh /home/docker/entry_point.sh

ENTRYPOINT ["sh"]

CMD ["/home/docker/entry_point.sh"]
