#!/usr/bin/env python3
"""Task 3: Deletion-resilient hypermedia pagination

This module provides a server class that can be used to retrieve pages of data
from a CSV file. The server class also provides a method to retrieve a
hyper-index, which is a data structure that contains the index of each item in
the dataset and the next index in the sequence.

"""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns the start and end indices of a page of data.

    The start index is the index of the first item on the page, and the end
    index is the index of the last item on the page.

    The start index is calculated as (page - 1) * page_size, and the end index
    is calculated as (page - 1) * page_size + page_size.

    Args:
        page (int): The page number.
        page_size (int): The page size.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices of the
            page of data.
    """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


class Server:

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes the server object.

        The server object is initialized with a cache that is used to store the
        dataset. The cache is a dictionary where the key is the index of each
        item in the dataset and the value is the data for that item.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Returns the dataset as a list of lists.

        The dataset is cached, so that it does not need to be reloaded every
        time a page is requested.

        The dataset is a list of lists, where each inner list represents a row
        in the dataset.

        Returns:
            List[List]: The dataset as a list of lists.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a page of data as a list of lists.

        The page of data is retrieved from the dataset, and the start and end
        indices of the page are calculated using the `index_range` function.

        Args:
            page (int): The page number. Defaults to 1.
            page_size (int): The page size. Defaults to 10.

        Returns:
            List[List]: The page of data as a list of lists.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a hyper-index as a dictionary.

        The hyper-index is a data structure that contains the index of each item
        in the dataset and the next index in the sequence.

        The hyper-index is retrieved from the indexed dataset, which is a
        dictionary where the key is the index of each item in the dataset and the
        value is the data for that item.

        Args:
            index (int): The index of the first item on the page. Defaults to
                None.
            page_size (int): The page size. Defaults to 10.

        Returns:
            Dict: The hyper-index as a dictionary.
        """
        data = self.indexed_dataset()
        assert index is not None and index >= 0 and index <= max(data.keys())
        page_data = []
        data_count = 0
        next_index = None
        start = index if index else 0
        for i, item in data.items():
            if i >= start and data_count < page_size:
                page_data.append(item)
                data_count += 1
                continue
            if data_count == page_size:
                next_index = i
                break
        page_info = {
            'index': index,
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data,
        }
        return page_info
