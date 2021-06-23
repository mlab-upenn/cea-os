from ceaos.sensors.temp_humidity import TempHumiditySensor


def setup_sensor() -> TempHumiditySensor:
    return TempHumiditySensor()


def test_creation():
    TempHumiditySensor()


def test_read():
    a = setup_sensor()
    assert (type(a.read_value()) == str)
