#!/usr/bin/env python3
"""make.fun bounty entry: Monday, Reviewed in One Line.

Monday, reviewed in one line. One star out of five,
and the review is generous.
"""

REVIEW = "Monday: arrived uninvited, stayed too long, broke the coffee machine, and left a meeting on my calendar — one star, would not recommend, will see again next week anyway."


def review():
    """Return Monday, reviewed in one line."""
    return REVIEW


def main():
    print(review())


if __name__ == "__main__":
    main()
