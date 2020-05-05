#!/usr/bin/env python3
"Multiple type anotations on a list"
from typing import List
mixed_list = List[float and int]


def sum_mixed_list(mxd_lst: mixed_list) -> float:
    """
    Takes a mixed list and returns the sum of the list
    sum_mixed_list([4.1, 2.6, 1]) = 7.7
    """
    result: float = 0

    for num in mxd_lst:
        result = result + num

    return result
