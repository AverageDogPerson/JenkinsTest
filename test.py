import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test case 1: Kiểm tra version
def test_get_version():
    response = client.get("/get_version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

# Test case 2: Kiểm tra số nguyên tố với số 2
def test_check_prime_2():
    response = client.get("/check_prime/2")
    assert response.status_code == 200
    assert response.json() == {"number": 2, "is_prime": True}

# Test case 3: Kiểm tra số nguyên tố với số 4
def test_check_prime_4():
    response = client.get("/check_prime/4")
    assert response.status_code == 200
    assert response.json() == {"number": 4, "is_prime": False}

# Test case 4: Kiểm tra số nguyên tố với số 17
def test_check_prime_17():
    response = client.get("/check_prime/17")
    assert response.status_code == 200
    assert response.json() == {"number": 17, "is_prime": True}

# Test case 5: Kiểm tra số nguyên tố với số 18
def test_check_prime_18():
    response = client.get("/check_prime/18")
    assert response.status_code == 200
    assert response.json() == {"number": 18, "is_prime": False}

# Test case 6: Kiểm tra số nguyên tố với số 1
def test_check_prime_1():
    response = client.get("/check_prime/1")
    assert response.status_code == 200
    assert response.json() == {"number": 1, "is_prime": False}

# Test case 7: Kiểm tra số nguyên tố với số 11
def test_check_prime_11():
    response = client.get("/check_prime/11")
    assert response.status_code == 200
    assert response.json() == {"number": 11, "is_prime": True}

# Test case 8: Kiểm tra số nguyên tố với số 25
def test_check_prime_25():
    response = client.get("/check_prime/25")
    assert response.status_code == 200
    assert response.json() == {"number": 25, "is_prime": False}

# Test case 9: Kiểm tra số nguyên tố với số 29
def test_check_prime_29():
    response = client.get("/check_prime/29")
    assert response.status_code == 200
    assert response.json() == {"number": 29, "is_prime": True}

# Test case 10: Kiểm tra số nguyên tố với số 100
def test_check_prime_100():
    response = client.get("/check_prime/100")
    assert response.status_code == 200
    assert response.json() == {"number": 100, "is_prime": False}
