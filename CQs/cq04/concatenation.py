"""Challenge question number four"""

__author__: str = "730735560"


def concat(choice1: str, choice2: str) -> str:
    """combines two strings"""
    return choice1 + choice2


if __name__ == "__main__":
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
