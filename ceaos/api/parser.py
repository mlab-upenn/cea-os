"""This file contains parsers for requests that come over the ZeroMQ wire"""
import json


def parse(msg, farm):
    decoded = json.loads(msg)
    if 'action' not in decoded:
        raise ValueError("No action declared")
    if 'cea-addr' not in decoded:
        raise ValueError("No target object specified")

    # We start by trying to find the target object

