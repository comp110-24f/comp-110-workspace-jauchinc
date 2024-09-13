"""Number guessing game CQ02"""

__author__: str == "730735560"  # type: ignore


def guess_a_number() -> None:
    secret: int = 7
    guess: int = int(input("Guess a number:"))  # Change input to int to make it work
    print("Your guess was " + str(guess))
    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is 7.")
    else:  # else now covers all other situations, i.e. greater than
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
