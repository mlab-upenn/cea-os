FROM python:3.8-slim

RUN mkdir /cea-os

COPY . /cea-os

RUN pip install --upgrade pip

WORKDIR /cea-os

RUN python3 setup.py install

CMD ls