import pytest

from pycalc.app import app


@pytest.fixture
def client():
    return app.test_client()


def test_index(client):
    respuesta = client.get("/")
    assert respuesta.status_code == 200
    assert respuesta.get_json()["app"] == "pycalc"


def test_add_endpoint(client):
    respuesta = client.get("/add/2/3")
    assert respuesta.status_code == 200
    assert respuesta.get_json() == {"resultado": 5.0}


def test_divide_by_zero_endpoint(client):
    respuesta = client.get("/divide/1/0")
    assert respuesta.status_code == 400


def test_unknown_operation(client):
    respuesta = client.get("/sqrt/2/3")
    assert respuesta.status_code == 404


def test_power_endpoint(client):
    respuesta = client.get("/power/2/3")
    assert respuesta.status_code == 200
    assert respuesta.get_json() == {"resultado": 8.0}

def test_power():
    assert calc.power(2, 3) == 8