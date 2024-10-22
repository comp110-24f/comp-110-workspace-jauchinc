"""EX05: List Unit Utils --> implementing list utility functions"""

__author__: str = "730735560"

list_2: list[int] = [1, 2, 3, 4, 5, 6]


def only_evens(list1: list[int]) -> list[int]:
    """Removes odd numbers from a list"""
    list2: list[int] = []
    for numbers in range(0, len(list1)):
        # I chose range because you need index to pop a value
        if (list1[numbers] % 2) == 0:
            # Modulo was used because it's the best and easiet way
            # To see if a number is even or odd by using the remainder
            # of a number divided by two
            list2.append(list1[numbers])
    # I had an issue with my index being out of range, but that was because popping a
    # Value out of list1 changed it length. To fix this, I added another empty list
    # That the even numbers can be added to instead of being removed from list1
    return list2


def sub(int_list: list[int], start: int, end: int) -> list[int]:
    """Makes a subset of a list between the start index and the end index minus 1"""
    sub_list: list[int] = []  # New list to not modify original
    if start < 0:
        start = 0
    if end > len(int_list):
        end = len(int_list)
    if (len(int_list) == 0) or (start >= len(int_list)) or (end <= 0):
        sub_list = []
    else:
        for values in range(start, (end)):
            sub_list.append(int_list[values])
    return sub_list


def add_at_index(list_1: list[int], element: int, index: int) -> None:
    """Adds element to list_1 at index"""
    if (index > len(list_1)) or index < 0:
        raise IndexError("Index is out of bounds for the input list")
    list_1.append(element)
    # Random number to add space at end
    idx_list: int = 1
    while (len(list_1) - idx_list) > index:
        list_1[(len(list_1) - idx_list)] = list_1[(len(list_1) - idx_list - 1)]
        idx_list += 1
    # It took me forever to figure out how to shift everything right
    # I tried using a for... in... loop with range, but that failed terribly
    # I decided that I needed to start from the end of the list so that
    # The mutated list wouldn't just be repeating numbers, because as each index
    # changes,
    # making the following one match it would just mean everything changes to the same
    # number
    # I used idx_list to determine how far from the end of the list the program should
    # go
    # to get the new values, but also for which value to use.
    list_1[index] = element
    return None
