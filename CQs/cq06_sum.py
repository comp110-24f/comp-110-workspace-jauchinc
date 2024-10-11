"""Summing the element of a list using different loops"""

__author__: str = "730735560"


def w_sum(vals: list[float]) -> float:
    """Uses a while loop to to sum every element in a list"""
    index: int = 0
    sum: float = 0
    # needed a variable for sum so there is somwhere to add values
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Uses a for loop to sum every element in a list"""
    sum: float = 0
    for numbers in vals:
        sum += numbers
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Uses a range and for loop to sum the elements in a list"""
    sum: float = 0
    for numbers in range(0, len(vals)):
        sum += vals[numbers]
    return sum
