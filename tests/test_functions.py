import pytest
import requests
import app


def test_function():
    # response = requests.post(
    #    "http://localhost:5000/calculate_integral",
    #    json={"function": "x", "a": 1, "b": 2},
    # )
    assert app.calculate_integral("x", 1, 2) == "3/2"


def test_determinant():
    matrix = [[3, 2, 3], [3, 4, 3], [4, 5, 4]]
    # response = requests.post(
    #    "http://localhost:5000/calculate_determinant",
    #    json={"matrix": matrix},
    # )
    assert app.calculate_determinant(matrix) == 0
