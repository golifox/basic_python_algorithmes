import random
from bubble import bubble_sort

EMPTY_LIST = list()
SINGLE_LIST = random.sample(range(-1_000, 1_000), 1)
SMALL_LIST = random.sample(range(-1_000, 1_000), 1_000)
BIG_LIST = random.sample(range(-10_000, 10_000), 10_000)


def test_bubble_empty():
    assert bubble_sort(EMPTY_LIST) == sorted(EMPTY_LIST)


def test_bubble_single():
    assert bubble_sort(SINGLE_LIST) == sorted(SINGLE_LIST)


def test_bubble_small():
    assert bubble_sort(SMALL_LIST) == sorted(SMALL_LIST)


def test_bubble_big():
    assert bubble_sort(BIG_LIST) == sorted(BIG_LIST)
