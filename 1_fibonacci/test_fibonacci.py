import os
import json
import random

from fibonacci import fib


def test_fibonacci():
    fib_file_path = os.path.join(os.path.abspath(os.curdir),
                                 'fibonacci_row.json')
    with open(fib_file_path, 'r') as f:
        fibonacci_row = json.load(f)

    random_int = random.randint(0, 999)
    assert fib(random_int) == fibonacci_row[str(random_int)]
