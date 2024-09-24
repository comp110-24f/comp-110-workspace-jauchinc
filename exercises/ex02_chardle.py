"""Wordle but the computer tells us where the letter is"""

__author__: str = "730735560"


def main() -> None:
    """Runs the code"""
    contains_char(word=(input_word()), letter=(input_letter()))


def input_word() -> str:
    """Asks user for a five-character word"""
    word_choice: str = input("Enter a 5-character word:")
    if len(word_choice) != 5:
        # I put this first because I felt like this wouldn't change but the else #
        # statement would a lot
        print("Error: Word must contain 5 characters.")
        exit()
    else:  # this  checks that the word length is 5
        print("'" + word_choice + "'")
    return word_choice  # can't return None, must be a str


def input_letter() -> str:  # same thing as input_word()
    """Asks user for a character"""
    character: str = input("Enter a single character:")
    if len(character) != 1:
        print("Error: Character must be a single character.")
        exit()  # I put this here because it happens after error prints, but only if
        # the condition is met, so won't interfere with the rest of the program
    else:
        print("'" + character + "'")
    return character


def contains_char(word: str, letter: str) -> None:
    """Tells how many occurrences of letter in word"""
    print("Searching for " + letter + " in " + word)
    count: int = 0
    if letter == word[0]:
        print(letter + " found at index 0")
        count += 1
    if letter == word[1]:
        print(letter + " found at index 1")
        count += 1
    if letter == word[2]:
        print(letter + " found at index 2")
        count += 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count += 1
    if letter == word[4]:
        # This was tricky. i originally but elif for everything which didn't work
        print(letter + " found at index 4")
        # if also shouldn't have an else because then it messes it up
        count += 1
    if count >= 1:
        print(str(count) + " instances of " + letter + " found in " + word)
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    if count == 1:
        print("1 instance of " + letter + " found in " + word)
    if count > 1:
        print(str(count) + " instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()
