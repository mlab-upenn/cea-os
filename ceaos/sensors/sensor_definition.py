"""
This file contains the basic interface for sensors in this code base.
"""
from ..analytics import Analytic


class Sensor:
    def __init__(self, location=None, analytics=None, name=None) -> None:
        self.analytics = analytics if analytics else list()
        self.location = location if location else ""
        self.name = name

    def read_value(self):
        """
        This method returns the value of the sensor
        """
        raise NotImplementedError

    def add_analytic(self, analytic: Analytic):
        """Add analytic to Sensor"""
        self.analytics += analytic

    def _process_analytics(self, value):
        """
        This function processes all of the analytics
        specified with the data provided.

        This function is backwards compatible, so it won't produce unexpected
        output in places where no analytics are requested.
        """
        if self.analytics:
            results = dict()
            results[self.location] = value
            for analytic in self.analytics:
                results[self.location + analytic.name] = analytic.analyze(value)
        else:  # If no analytics are defined, just don't compute anything
            results = value
        return results

    def calibrate(self):
        """
        This method is used to calibrate the sensor.
        Need not be implemented for sensors that don't require calibration
        """
        raise NotImplementedError
