import pytest
from ceaos.actuators import NetworkActuator
from threading import Thread


def test_creation():
    NetworkActuator('127.0.0.1', '2048')


def test_recv_bool():
    import zmq
    import json
    from time import sleep

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:2048")

    NA = NetworkActuator('127.0.0.1', '2048')
    t = Thread(target=NA.do, args=(True,), daemon=True)
    t.start()

    sleep(1)  # Wait to ensure message was sent from NA

    r_msg = json.loads(socket.recv_string(flags=zmq.NOBLOCK))
    socket.send_string(json.dumps({'response': 'Valid Test', 'status': 200}))

    assert r_msg == {'action': 'do', 'payload': True}


def test_recv_float():
    import zmq
    import json
    from time import sleep

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:2048")

    NA = NetworkActuator('127.0.0.1', '2048')
    t = Thread(target=NA.do, args=(10.1,), daemon=True)
    t.start()

    sleep(1)  # Wait to ensure message was sent from NA

    r_msg = json.loads(socket.recv_string(flags=zmq.NOBLOCK))
    socket.send_string(json.dumps({'response': 'Valid Test', 'status': 200}))

    assert r_msg == {'action': 'do', 'payload': 10.1}


def test_recv_dict():
    import zmq
    import json
    from time import sleep

    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:2048")

    NA = NetworkActuator('127.0.0.1', '2048')
    payload = {'A': True, "B": 'test_text', 'C': 10.2135}
    t = Thread(target=NA.do, args=(payload,), daemon=True)
    t.start()

    sleep(1)  # Wait to ensure message was sent from NA

    r_msg = json.loads(socket.recv_string(flags=zmq.NOBLOCK))
    socket.send_string(json.dumps({'response': 'Valid Test', 'status': 200}))

    assert r_msg == {'action': 'do', 'payload': {'A': True,
                                                 "B": 'test_text',
                                                 'C': 10.2135}}
