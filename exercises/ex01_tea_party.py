"""Planning a cozy tea party using a Program."""

__author__: str = "730749279"


def main_planner(guests: int) -> None:
    """Calls all functions we just defined."""
    # Add "main" functions at the upper portion of a program.
    # "Main" functions commonly output but do not return values.
    # None does not need a return statement.
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Determining the number of tea bags needed."""
    return 2 * people


def treats(people: int) -> int:
    """Determining the number of treats based on number of tea bags needed."""
    # Unsure of correct formatting of assignment operator.
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Determining the total cost of tea bags and treats."""
    return tea_count * 0.50 + treat_count * 0.75
    # Tried setting tea_count equal to tea_bags.
    # This led to miscalculations.


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
    # If you place the conditional statement above,
    # the program will call the main_planner first.
