import zmq
import json
import logging


class NetworkActuator:
    def __init__(self, device_ip, port) -> None:
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(f"tcp://{device_ip}:{port}")
        self.datatype = None
        self.location = None
        self.name = None
        self.refresh_rate = None

    def setpoint(self, arg):
        message = {
            'action': 'setpoint',
            'payload': arg
        }
        self.socket.send_string(json.dumps(message))
        reply = self.socket.recv()
        reply = json.loads(reply)
        logging.debug("Network Actuation conducted, reply: {}".format(reply))
        return reply

    def do(self, arg):
        message = {
            'action': 'do',
            'payload': arg
        }
        self.socket.send_string(json.dumps(message))
        reply = self.socket.recv()
        reply = json.loads(reply)
        logging.debug("Network Actuation conducted, reply: {}".format(reply))
        return reply

    def calibrate(self):
        """
        This method is used to calibrate the actuator.
        Need not be implemented for actuators that don't require calibration
        """
        pass
