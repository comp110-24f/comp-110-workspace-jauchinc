"Quiz 04 Review"

__author__: str = "730735560"


def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    """Determine if all dogs were good in daycare."""
    is_good: bool = int(scores[idx]["score"]) >= thresh
    is_last: bool = idx == len(scores) - 1
    if is_good:
        print(f"Good dog, {scores[idx]["name"]}")
        if is_last:
            return True
        else:
            return all_good(scores, thresh, idx + 1)
    else:
        return False
