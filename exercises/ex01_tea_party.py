"""How much for a tea party?"""

__author__: str = "730735560"


def main_planner(guests: int) -> None:
    """Displaying counts for each variable"""
    print(
        "A Cozy Tea Party for "
        + str(guests)
        + " People!"
        + "\n"
        + "Tea Bags: "
        + str(tea_bags(people=guests))
        + "\n"
        + "Treats: "
        + str(treats(people=guests))
        + "\n"
        + "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )  # /n makes line breaks
    # Convert everything to proper time value!


def tea_bags(people: int) -> int:
    """How many tea bags to buy"""
    return people * 2


def treats(people: int) -> int:
    """How many treats to get"""
    return int(
        (tea_bags(people=people)) * 1.5
    )  # make sure to conver to return value (int)


# remember how to do math ;)
# Variables can = themselves


def cost(
    tea_count: int, treat_count: int
) -> (
    float
):  # sometimes trailblazer and/or VS studios has to be restarted for code to work
    """Cost of tea party"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
