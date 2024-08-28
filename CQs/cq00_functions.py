"""The first Challenge Question in COMP110"""

_author_ = "730735560"


def mimic(message: str) -> str:
    """It's like an echo, echo, echo, cho..."""
    return message


def main() -> None:
    """Main"""
    print(mimic(message=input("What is your message?")))
    return None


if __name__ == "__main__":
    main()
