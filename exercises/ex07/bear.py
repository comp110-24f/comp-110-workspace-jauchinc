"""File to define Bear class."""

__author__: str = "730735560"


class Bear:
    """This is a bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes age and hunger."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Ages a bear and makes it hungry."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Helps a bear eat."""
        self.hunger_score += num_fish
        return None
