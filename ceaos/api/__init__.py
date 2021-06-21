"""This module contains components """
import json
import zmq
import logging

from .parser import parse


def create_api(farm):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:23267")  # This is ceaos on a E.161 pad

    while True:
        request = socket.recv()

        # Parse the request

        response = parse(request, farm)

        logging.info("Request handled: {}".format(request))
        socket.send(json.dumps({'response': response}))
