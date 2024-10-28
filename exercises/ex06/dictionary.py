"""EX06 Dictionary Utility Functions"""

__author__: str = "730735560"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Switches keys and values to make a new dictionary"""
    dictionary_2: dict[str, str] = {}
    values: list[str] = []
    # Make a new dictionary to put new values and keys in
    for keys in dictionary:
        for vals in values:
            if vals == dictionary[keys]:
                raise KeyError("Cannot have duplicate keys")
        values.append(dictionary[keys])
        dictionary_2[dictionary[keys]] = keys
    return dictionary_2


def favorite_color(names_colors: dict[str, str]) -> str:
    """Returns the color that occurs most frequently"""
    color_count: dict[str, int] = {}
    # This dictionary is to count each color's occurrence
    for names in names_colors:
        color = names_colors[names]
        # This is so I don't count the names but instead the colors
        if color in color_count:
            color_count[color] += 1
        # Sees if colors already occur in color_count
        else:
            color_count[color] = 1
    favorite: str = ""
    # This will be the most frequent color in the end
    max_number: int = 0
    # Keeps track of most common color
    for counts in color_count:
        if color_count[counts] > max_number:
            max_number = color_count[counts]
            favorite = counts
    return favorite


def count(values: list[str]) -> dict[str, int]:
    """Counts how many times each value occurs in values"""
    counts: dict[str, int] = {}
    for strings in values:
        if strings in counts:
            counts[strings] += 1
        else:
            counts[strings] = 1
    # This is similar to what i did in favorite_color to see
    # if a value is in the dict already
    return counts


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Alphabetizes the words in a list and puts them with their corresponding
    letter in a dict"""
    alphabetical: dict[str, list[str]] = {}
    for strings in words:
        if strings[0].lower() in alphabetical:
            alphabetical[strings[0].lower()] += [strings]
        else:
            alphabetical[strings[0].lower()] = [strings]
    # This used a similar method to the previous functions to add
    # Certain values to a dictionary, so I repeated that method
    return alphabetical


def update_attendance(log: dict[str, list[str]], day: str, student: str) -> None:
    """Updates the attendance log with the student and the day they were there"""
    if day in log:
        if student not in log[day]:
            log[day].append(student)
    else:
        log[day] = [student]
    # Once again, very similar to previously used methods
