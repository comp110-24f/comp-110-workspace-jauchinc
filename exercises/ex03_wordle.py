"""Making my own Wordle game"""

__author__: str = "730735560"


def main(secret: str) -> None:
    """The entrypoint of the program and the main game loop."""
    turn_number: int = 1  # var to keep track of turns
    while turn_number < 7:
        print(f"=== Turn {turn_number}/6 ===")
        choice: str = input_guess(len(secret))
        # I made this a variable to be easier to manage and also
        # So that input_guess wouldn't print over and over and over
        # Without providing actual results
        emojified(guess=choice, secret=secret)
        # Trying to figure out where to incorporate input_guess was hard
        # Figured out it could be nested in emojified
        if choice == secret:
            print(f"You won in {turn_number}/6 turns!")
            turn_number += 8 - turn_number
            # 8 was arbitrary and so that turn_number would be > 7 without == 7
        else:
            turn_number += 1
    if turn_number == 7:
        print("X/6 - Sorry, try again tomorrow!")
        return


def input_guess(num_char: int) -> str:
    """Asks the player to guess a word"""
    guess: str = input(f"Enter a {str(num_char)} character word: ")
    while len(guess) != num_char:  # i had to call the parameter within the function def
        # this works but is different than we've done
        guess = input(f"That wasn't {str(num_char)} chars! Try again: ")
    return guess


def contains_char(input_word: str, input_char: str) -> bool:
    """Tests to see if the character is in the word"""
    assert len(input_char) == 1
    idx: int = 0
    count: int = 0
    # I need to create a variable that keeps
    # track of if there is an occurrence of the character
    present: bool = True
    # I also needed a variable to return that was a bool
    while idx < len(input_word):  # want it to loop through the word once
        if input_char == input_word[idx]:
            count += 1
            idx += 1
        else:
            idx += 1
    if count == 0:
        present = False
    else:
        present = True
    return present


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Compares two strings of equal lengths and tells us what matches"""
    assert len(guess) == len(secret)
    index: int = 0
    score: str = ""  # this is the string within which the blocks will be concatenated
    while index < len(guess):
        if guess[index] == secret[index]:
            score += GREEN_BOX
            index += 1
        elif contains_char(secret, guess[index]):
            # I couldn't get the yellow squares to work because
            # I had contains_char == True. I took True away and it worked
            # It's implied that contains_char is true
            score += YELLOW_BOX
            index += 1
        else:
            score += WHITE_BOX
            index += 1
    print(score)
    return score


if __name__ == "__main__":
    main(secret="codes")
