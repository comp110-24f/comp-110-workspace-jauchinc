"""Unit tests practice"""

__author__: str = "730735560"


def find_and_remove_max(list: list[int]) -> int:
    """Find and returns the largest number and also removes it"""
    max_number: int = 0
    index: int = 0
    if len(list) == 0:
        max_number = -1
    else:
        for numbers in range(0, len(list)):
            # I used range so I could use the index of the list
            # rather than the actual value at that index
            if list[numbers] >= max_number:
                max_number = list[numbers]
            # I didn't add the value to max_number because
            # then it would be the sum of the highest numbers
        while index < len(list):
            if list[index] == max_number:
                list.pop(index)
            index += 1
    return max_number
