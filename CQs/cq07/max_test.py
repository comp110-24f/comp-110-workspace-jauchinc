"""Practicing unit tests"""

__author__: str = "730735560"

from CQs.cq07.find_max import find_and_remove_max

list_test: list[int] = [1, 6, 8, 1, 8, 2, 8]
list_test2: list[int] = [1, 10, 2, 10, 4, 10, 6]
list_test3: list[int] = []
# These are to test the


def test_output():
    assert find_and_remove_max(list_test) == 8


def test_mutation():
    find_and_remove_max(list_test2)
    assert list_test2 == [1, 2, 4, 6]


def test_weird_output():
    assert find_and_remove_max(list_test3) == -1
