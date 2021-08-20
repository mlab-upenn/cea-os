""" This contains the interface for analytics """


class Analytic:
    """
    Interface for analytic operations that
    take place on the output of a sensor
    """
    def __init__(self, name) -> None:
        self.name = name

    def analyze(self, sensor_reading):
        """
        This function takes in a sensor reading, and returns the analyzed data.
        """
        raise NotImplementedError
