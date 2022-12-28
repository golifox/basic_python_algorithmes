'''
Array 1000 elements: 
    Function bubble_sort Took 0.8730 seconds

Array 10000 elements:
    Function bubble_sort Took ~ 38 seconds
      
'''

from copy import deepcopy
import numpy as np
from typing import Iterable

from exec_time import timeit


@timeit
def bubble_sort(values: Iterable) -> None:
    length: int = len(values)
    swapped: bool = False

    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if values[j] > values[j + 1]:
                swapped = True
                values[j], values[j + 1] = values[j + 1], values[j]

        if not swapped:
            return
