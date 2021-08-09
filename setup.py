from setuptools import setup

setup(
    name='ceaos',
    version='0.0.1',
    packages=['ceaos'],
    install_requires=[
        'requests',
        'build',
        'influxdb',
        'pyzmq',
        'importlib_resources',
        'PyYAML',
        'pigpio',
        'plantcv'
    ],
)
