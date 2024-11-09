"""File to define River class."""

__author__: str = "730735560"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """This is a river."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """If fish or bears are too old, then they are removed."""
        new_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        self.fish = new_fish
        new_bears: list[Bear] = []
        for bears in self.bears:
            if bears.age <= 5:
                new_bears.append(bears)
        self.bears = new_bears
        # Took me a second to realize I should use a loop
        # But I figured it out then copied the fish code
        # And replaced it with bears
        return None

    def remove_fish(self, amount: int) -> None:
        """Removes a certain amount of fish from the beginning of self.fish."""
        not_eaten_fish: list[Fish] = []
        for fish in range(amount, len(self.fish)):
            not_eaten_fish.append(self.fish[fish])
        self.fish = not_eaten_fish
        return None

    def bears_eating(self):
        """Bears eat, but no more than three fish if there are more than 5."""
        for bears in self.bears:
            if len(self.fish) >= 5:
                Bear.eat(bears, 3)
                # I had an issue with self, because there is no self
                # value for bears in this function. I figured it out
                # by having self be each value in the bears list
                self.remove_fish(3)
        return None

    def check_hunger(self):
        """Sees if any bears have starved to death yet."""
        healthy_bears: list[Bear] = []
        for bears in self.bears:
            if bears.hunger_score >= 0:
                healthy_bears.append(bears)
        self.bears = healthy_bears
        return None

    def repopulate_fish(self):
        """Makes fish babies."""
        guppies: int = len(self.fish) // 2 * 4
        for _ in range(0, guppies):
            self.fish.append(Fish())
        # Used this to add the new fish, since it worked in the beginning
        return None

    def repopulate_bears(self):
        """Makes bear babies."""
        cubs: int = len(self.bears) // 2
        for _ in range(0, cubs):
            self.bears.append(Bear())
        # Used this to add the new bears, since it worked in the beginning
        return None

    def view_river(self):
        """Tells you what day it is in the river and how many fish a bears there are."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Calls one_river_day seven times."""
        number: int = 1
        while number <= 7:  # Couldn't figure out how to do this
            # then realized I had to use self.the_function to call
            # it in another method
            self.one_river_day()
            number += 1
        return None
