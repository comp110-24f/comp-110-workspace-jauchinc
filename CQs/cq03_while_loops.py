"""While loops practice"""

__author__: str = "730735560"


def num_instances(
    phrase: str, search_char: str
) -> None:  # returns None because you don't have to remember the return value
    """Counts how many times a letter appears in a word"""
    count: int = 0
    indphrase: int = 0
    while indphrase < len(
        phrase
    ):  # indphrase cannot be <= to len(phrase) because it would get to the last character and the not have anywhere to go
        if search_char == phrase[indphrase]:
            count += 1
            indphrase += 1  # both if and else have it add one to indphrase to move on to next letter
        else:
            indphrase += 1
    print(count)
    return None  # this isn't necessary but helps me organize my thoughts
