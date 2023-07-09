#!/usr/bin/env python3
""" complex types - list of float
"""


from typing import List

Input = List[float]


def sum_list(input_list: Input) -> float:
    return sum(input_list)
