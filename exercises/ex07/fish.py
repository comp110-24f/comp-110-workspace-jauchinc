"""File to define Fish class."""

__author__: str = "730735560"


class Fish:
    """This is a fish."""

    age: int

    def __init__(self):
        """Initializes age."""
        self.age = 0
        return None

    def one_day(self):
        """Ages fish."""
        self.age += 1
        return None
