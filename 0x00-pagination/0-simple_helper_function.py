#!/usr/bin/env python3
"""
function to determine index range
"""
from typing import Tuple


def index_range(page: int, page_size: int):
    """
    func to cal index range
    args :
    page: the page number
    page_size: the number of items
    """
    start_index = (page - 1) * page_size
    end = start_index + page_size
    return (start_index, end)
