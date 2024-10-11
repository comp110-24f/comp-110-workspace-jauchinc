"""Mutating functions."""

__author__: str = "730735560"


def manual_append(list: list[int], number: int) -> None:
    """Adds a number to list"""
    list.append(number)
    # This was fairly easy but took me a second to realize list
    # could just equal an empty list


def double(num_list: list[int]) -> None:
    """Doubles each item of the list"""
    idx: int = 0
    while idx < len(num_list):
        (num_list[idx]) = num_list[idx] * 2
        # I had to go back through my notes to remember
        # I couldn't just multiply the index by two but
        # Had to set it equal to itself times two
        idx += 1
    return


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
