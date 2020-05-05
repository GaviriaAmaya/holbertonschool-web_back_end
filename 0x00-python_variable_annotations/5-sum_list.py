#!/usr/bin/env python3
"Complex type anotations"
from typing import List
float_list = List[float]


def sum_list(input_list: float_list) -> float:
    """
    Takes a list of floats and returns the sum of the list
    sum_list([4.1, 2.6, 1.0]) = 7.7
    """
    result: float = 0

    for num in input_list:
        result = result + num

    return result
