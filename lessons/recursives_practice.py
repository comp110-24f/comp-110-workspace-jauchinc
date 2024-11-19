# Factorial
def factorial(n: int) -> int:  # type: ignore
    """Calculates factorial of int n"""
    # Edge case
    if n < 1:
        return -1
    # Base case
    if n == 1 or 0:
        return 1
    # Recursive case
    if n > 1:
        return n * factorial(n - 1)
