FROM python:3.7.4-slim-buster

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install htop curl git

RUN pip install flask
COPY . ./
WORKDIR ./
RUN python setup.py install

EXPOSE 5000
WORKDIR /ivybranch/app
CMD ["python", "server.py"]