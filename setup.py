from setuptools import setup

setup(
    name='ceaos',
    version='0.0.1',
    packages=['ceaos'],
    install_requires=[
        'requests',
        'build',
        'influxdb',
        'importlib_resources',
        'PyYAML'
    ],
)
