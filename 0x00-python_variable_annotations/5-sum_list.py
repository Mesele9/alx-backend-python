#!/usr/bin/env python3
""" complex types - list of float
"""


from typing import List

Input = List[float]


def sum_list(input_list: Input) -> float:
    """
    a type-annotated function sum_list which takes a list input_list of
    floats as argument and returns their sum as a float.
    """
    return sum(input_list)
