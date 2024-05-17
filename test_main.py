from fastapi import status
from fastapi.testclient import TestClient

from .main import MAX_K, MIN_K, app, calculate_probabilities, calculate_probability


def test_calculate_probability():
    assert round(calculate_probability(MIN_K), 12) == 0.545454545455
    assert round(calculate_probability(MAX_K), 12) == 0.502538071066


def test_calculate_probabilities():
    probabilities = calculate_probabilities()
    assert len(probabilities) == MAX_K - MIN_K + 1
    assert probabilities[0] == calculate_probability(MIN_K)
    assert probabilities[MAX_K - MIN_K] == calculate_probability(MAX_K)


client = TestClient(app)


def test_get_probabilities():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == MAX_K - MIN_K + 1
    response = client.get("/", headers={"k": "9"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == calculate_probability(9)
