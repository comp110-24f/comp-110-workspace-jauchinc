"""Exploring linked list utils in class."""

from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        self.value = val
        self.next = next

    def __str__(self) -> str:
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
    """Returns the value of the node at the index in the recursive list"""
    index -= 1
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index > 0:
        return value_at(head.next, index)
    if index == 0:
        return head.value


def last(head: Node) -> int:
    """Returns the last Node in a linked list."""
    if head.next is None:  # Base case
        return head.value
    else:
        return last(head.next)


two: Node = Node(2, None)
one: Node = Node(1, two)
print(one)
print(last(one))
