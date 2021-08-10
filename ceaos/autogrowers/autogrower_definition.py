"""
This file contains the basic interface for autogrowers in this code base.
"""


class Auto_Grower:
    def __init__(self) -> None:
        self.inputs = dict()
        self.outputs = dict()

    def control(self):
        raise NotImplementedError
