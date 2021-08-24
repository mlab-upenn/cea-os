from .autogrower_definition import Auto_Grower
import pywemo
import datetime

# Time Grower should only be used for actuation that needs
# to be controlled based on time of day
class TimeGrower(Auto_Grower):
    def __init__(self, name=None):
        self.inputs = dict()
        self.outputs = dict()
        self.refresh_rate = None
        self.name = name

    def add_inputs(self, name, input):
        self.inputs[name] = input

    def add_outputs(self, name, output):
        self.outputs[name] = output

    def control(self):
        for output in self.outputs:
            self.outputs[output].do()
