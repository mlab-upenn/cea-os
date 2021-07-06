FROM python:3.8-slim

EXPOSE 23267/tcp

RUN mkdir /ceaos

COPY . /ceaos

RUN pip3 install --upgrade pip

WORKDIR /ceaos

RUN python3 setup.py develop

CMD python3 -u scripts/runner.py
