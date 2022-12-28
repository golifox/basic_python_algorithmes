'''
Having number 0 < n < 40 calculate N Fibonacci number.
'''
from functools import cache
import sys
import json


@cache
def fib(n: int) -> int:
    before_value, last_value = 0, 1

    if n == 0:
        return 0

    if n == 1:
        return 1

    for _ in range(1, n):
        before_value, last_value = last_value, before_value + last_value

    return last_value
