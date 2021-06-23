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
        try:
            request = socket.recv()

            # Parse the request

            try:
                response = parse(request, farm)
                logging.info("Request handled: {}".format(request))

            except TypeError as e:
                response = "Request encountered error: {}".format(e)
                logging.info(
                    "Request {} encountered payload error {}".format(request, e)
                )

            socket.send(json.dumps({"response": response}))

        except KeyboardInterrupt:
            # We're being compelled to shutdown. Let's terminate gracefully
            socket.close()
            context.term()
