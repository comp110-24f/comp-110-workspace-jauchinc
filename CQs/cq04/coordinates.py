"""Challenge question number four"""

__author__: str = "730735560"


def get_coords(xs: str, ys: str) -> None:
    "prints the formatted pairs of each character"
    idx: int = 0
    idy: int = 0
    while idx < len(xs):
        while idy < len(ys):
            print("(" + xs[idx] + "," + ys[idy] + ")")
            idy += 1
        idy = 0  # idy has to be reset so that the second while loop works
        idx += 1
    # i had to work on this one a bit.
    # I found that you can just put a while loop right under another
    # I also realized that I would need two variables for the index, a y and x
    return
