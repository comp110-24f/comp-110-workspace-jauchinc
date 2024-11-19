"""Explorinng linked list utils in class."""

from __future__ import annotations

__author__: str = "730735560"


class Node:
    """Node class!"""

    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        """Initializes the Node."""
        self.value = val
        self.next = next

    def __str__(self) -> str:
        """Magic method."""
        rest: str = ""
        if self.next is None:  # Base case
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


def recursive_range(start: int, end: int) -> Node | None:
    """Creates linked list w/ values from start to end."""
    # Edge case
    if start > end:
        raise ValueError("Start cannot be greater than end")
    # Base case
    if start == end:
        return None
    # Recursive case -- call function again!!
    else:
        first: int = start
        rest: Node | None = recursive_range(start + 1, end)
        return Node(first, rest)


def value_at(head: Node | None, index: int) -> int | None:
    """Returns the value of the node at the index in the recursive list."""
    index -= 1  # This makes sure that index is keeping track of each time
    # we cycle through value_at again
    if head is None:  # When head is None, then the list is empty
        raise IndexError("Index is out of bounds on the list.")
    if index > -1:  # Since indexing starts at 0, we have to start at -1
        # with regular ints to make sure that we obtain the right value
        return value_at(head.next, index)
    if index == -1:
        return head.value


def max(head: Node | None) -> int:
    """Finds the max value in the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None.")
    maximum: int = 0
    if head.value > maximum:
        maximum = head.value
        if head.next is not None:
            if max(head.next) > maximum:  # I had so much trouble trying to save
                # maximum each time so that if something after the first value
                # was greater, then it would change it to that.
                # I solved this problem by remembering that max returns and int
                # so if that int is greater than maximum, I just had to set maximum
                # equal to it. That being said, I just had to compare the return of
                # max(head.next) to maximum.
                maximum = max(head.next)
    return maximum


def linkify(Nodes_list: list[int]) -> Node | None:
    """Creates a Linked List of Nodes out of a regular list."""
    if len(Nodes_list) == 0:
        return None
    my_node: Node | None = Node(
        Nodes_list[0], linkify(Nodes_list[1:])
    )  # The slice shortens the list each time
    return my_node  # I had it printed, but that messed up
    # the nodes each time, printing them individually


def scale(head: Node | None, factor: int) -> Node | None:
    """Multiplies the values in a linked list by the factor."""
    if head is None:
        return None
    node: Node | None = Node(head.value * factor, scale(head.next, factor))
    return node


def last(head: Node) -> int:
    """Finds the last value in the linked list."""
    if head.next is None:  # Base case
        return head.value
    else:
        return last(head.next)


two: Node = Node(2, None)
one: Node = Node(1, two)
print(one)
print(last(one))
