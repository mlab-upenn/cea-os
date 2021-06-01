from setuptools import setup

setup(
    name='cea-os',
    version='0.0.1',
    packages=['cea-os'],
    install_requires=[
        'requests',
        'build',
        'influxdb'
    ],
)
