"""Exercise 4 --> practice with list utils"""

__author__: str = "730735560"


def all(number_list: list[int], number: int) -> bool:
    """Lets us know if a list is only one number"""
    within: bool = True
    if len(number_list) == 0:
        within = False
    for elem in number_list:
        # used this to cycle through quickly
        if elem != number:
            within = False
            # This only changes within if it needs to be false
            # This way, if one number matches, it doesn't switch to true
    return within


def max(max_list: list[int]) -> int:
    """Finds the largest number in a list"""
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    max_number: int = max_list[0]
    for numbers in range(0, len(max_list)):
        # I used range so I could use the index of the list
        # rather than the actual value at that index
        if max_list[numbers] > max_number:
            max_number = max_list[numbers]
            # I didn't add the value to max_number because
            # then it would be the sum of the highest numbers
    return max_number


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Determines if two lists are completely equal"""
    equal: bool = True
    if len(list_1) != len(list_2):  # this is to account for length variable
        equal = False  # If was used to skip the next step if the two are not equal
    else:
        for numbers in range(0, len(list_1)):  # once again, this was to use the index
            # rather than the actual value at that index
            if list_1[numbers] != list_2[numbers]:
                equal = False
    return equal


def extend(list1: list[int], list2: list[int]) -> None:
    """Adds to lists together"""
    for numbers in list2:
        list1.append(numbers)
        # I did this rather than just append list2 to list1 because
        # We want to only append the values, not the list itself
    return
