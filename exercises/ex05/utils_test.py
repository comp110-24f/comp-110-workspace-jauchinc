"""EX05: List Unit Utils --> testing list utility functions"""

__author__: str = "730735560"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index

# only_evens

odd_example: list[int] = [1, 3, 5, 7]
regular_example: list[int] = [1, 2, 3, 4, 5, 6]
regular_example_2: list[int] = [1, 2, 3, 4, 5, 6]


def test_for_only_odds() -> None:
    """Tests if only odds are input"""
    assert only_evens(odd_example) == []


def test_for_output_evens() -> None:
    """Tests a regular input"""
    assert only_evens(regular_example) == [2, 4, 6]


def test_for_mutation() -> None:
    """Tests to see if the input list is mutated"""
    only_evens(regular_example_2)
    assert regular_example_2 == [1, 2, 3, 4, 5, 6]


# sub

negative: list[int] = [1, 2, 3, 4, 5, 6]
regular: list[int] = [7, 8, 9, 10, 11]
regular_2: list[int] = [2, 4, 6, 8, 10, 12]


def test_negative_start() -> None:
    """Tests response if the start variable is negative"""
    assert sub(negative, -2, 4) == [1, 2, 3, 4]


def test_for_regular_output() -> None:
    """Tests a regular input for a regular output"""
    assert sub(regular, 1, 4)


def test_sub_mutation() -> None:
    """Tests to see if the input list is mutated"""
    sub(regular_2, 3, 5)
    assert regular_2 == [2, 4, 6, 8, 10, 12]


# add_at_index

large_index: list[int] = [1, 2, 3]
normal_input: list[int] = [1, 2, 3, 4, 5, 6]
normal_mutation: list[int] = [1, 2, 3, 4, 5, 6]


def test_index_too_big() -> None:
    """Tests to make sure IndexError is raised for too big a index"""
    with pytest.raises(IndexError):
        assert (
            add_at_index(large_index, 4, 12)
            == "Index is out of bounds for the input list"
        )


def test_normal_input() -> None:
    """Makes sure that the function returns None"""
    assert add_at_index(normal_input, 8, 2) == None


def test_mutation_of_list() -> None:
    """Tests to see if the function did mutate the list like it should"""
    add_at_index(normal_mutation, 8, 2)
    assert normal_mutation == [1, 2, 8, 3, 4, 5, 6]
