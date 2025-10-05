import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

def client():
    return app.test_client()

def test_root_ok():
    r = client().get("/")
    assert r.status_code == 200
    assert "you called" in r.get_data(as_text=True)

def test_echo_form_ok():
    r = client().post("/echo", data={"text": "Hello Phil!"})
    assert r.status_code == 200
    assert r.get_data(as_text=True) == "You said: Hello Phil!"

def test_factors_prime_13():
    r = client().get("/factors?inINT=13")
    assert r.status_code == 200
    assert r.get_json()["factors"] == [13]

def test_factors_composite_12_matches_spec():
    r = client().get("/factors?inINT=12")
    assert r.status_code == 200
    assert r.get_json()["factors"] == [1, 2, 2, 3]

def test_factors_missing_param():
    r = client().get("/factors")
    assert r.status_code == 400

def test_factors_non_integer():
    r = client().get("/factors?inINT=abc")
    assert r.status_code == 400

def test_factors_too_small():
    r = client().get("/factors?inINT=1")
    assert r.status_code == 400
