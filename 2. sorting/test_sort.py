import pytest

from bubble import bubble_sort
from constants import *

def test_bubble_empty():
    assert bubble_sort(EMPTY_LIST) == sorted(EMPTY_LIST)


def test_bubble_single():
    assert bubble_sort(SINGLE_LIST) == sorted(SINGLE_LIST)


def test_bubble_small():
    assert bubble_sort(SMALL_LIST) == sorted(SMALL_LIST)


def test_bubble_big():  
    assert bubble_sort(BIG_LIST) == sorted(BIG_LIST)
