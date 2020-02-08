FROM python:3.7
MAINTAINER EbichanOO

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN mkdir ./codes
WORKDIR /codes
COPY requirements.txt .
COPY server.py .
COPY ./params/entity_vector/entity_vector.model.bin ./params/entity_vector/

RUN pip install -r requirements.txt

EXPOSE 8080
CMD [ "python","server.py" ]