#!/usr/bin/env python3

"""
Module 2-hypermedia_pagination
This module provides functionality for paginating a dataset of popular baby names.
"""

import csv
import math
from typing import List

def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end indexes for a page of data.
    
    Args:
        page (int): The page number, starting from 1.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end indexes.
    """
    return page_size * (page - 1), page * page_size

class Server:
    """
    Server class to handle loading and paginating a dataset.
    """
    
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the Server instance.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load the dataset from a CSV file if not already loaded.
        
        Returns:
            List[List]: The dataset as a list of lists.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of data from the dataset.
        
        Args:
            page (int): The page number, starting from 1.
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of data for the specified page.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        start, end = index_range(page, page_size)
        try:
            data = self.dataset()
            return data[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Get a dictionary containing pagination information.
        
        Args:
            page (int): The page number, starting from 1.
            page_size (int): The number of items per page.

        Returns:
            dict: A dictionary containing pagination metadata and data.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
