import pytest

from pairer.pairer import Pairer


@pytest.mark.parametrize("test_case", [
    {
        "values": [4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0],
        "expected": {4: 4, 12: 4, 8: 2, 0: 2, 9: 1, 1: 1, 2: 1, 11: 1},
    },
    {
        "values": [1, 2, 6],
        "expected": {1: 1, 2: 1, 6: 1},
    }
])
def test_count_nums(test_case):
    pairer = Pairer(test_case["values"], 12)
    result = pairer.count_nums(test_case["values"])
    assert sorted(test_case["expected"]) == sorted(result)


@pytest.mark.parametrize("test_cases", [
    {
        "values": [4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0],
        "target": 12,
        "expected": [[0, 12], [4, 8], [4, 8], [1, 11], [0, 12]]
    },
    {
        "values": [1, 2, 6],
        "target": 5,
        "expected": []
    },
    {
        "values": [1, 6, 6, 5, 8, 10, 100, 13],
        "target": 12,
        "expected": [[6, 6]]
    },
    {
        "values": [1, 6, 6, 6, 5, 8, 10, 100, 13],
        "target": 12,
        "expected": [[6, 6]]
    },
    {
        "values": [1, 6, 6, 6, 6, 8, 10, 100, 13],
        "target": 12,
        "expected": [[6, 6], [6, 6]]
    },
])
def test_compute(test_cases):
    pairer = Pairer(test_cases['values'], test_cases['target'])
    result = pairer.compute()
    assert sorted(test_cases['expected']) == sorted(result)
