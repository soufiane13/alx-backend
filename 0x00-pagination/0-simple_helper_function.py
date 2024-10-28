#!/usr/bin/env python3
"""Pagination helper function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index of a page given the page number and page size.

    Args:
        page (int): The page number. Page numbers start at 1.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end index of the page.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
