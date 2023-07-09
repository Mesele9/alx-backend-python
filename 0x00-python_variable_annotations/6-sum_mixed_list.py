#!/usr/bin/env python3
""" annotated mixed list"""


from typing import List, Union

MixedList = List[Union[float, int]]


def sum_mixed_list(mxd_lst: MixedList) -> float:
    """ a type-annotated function sum_mixed_list which takes a list mxd_lst
    of integers and floats and returns their sum as a float. """
    return sum(mxd_lst)
