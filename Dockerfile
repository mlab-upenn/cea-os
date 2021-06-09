FROM python:3.8-slim

RUN mkdir /ceaos

COPY . /ceaos

RUN pip install --upgrade pip

WORKDIR /ceaos

RUN python3 setup.py install

CMD ls