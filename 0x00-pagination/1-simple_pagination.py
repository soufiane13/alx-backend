#!/usr/bin/env python3
"""Simple pagination sample.

This sample demonstrates a simple pagination using a CSV file as the data source.
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate the start and end indices for the given page and page size.

    Args:
        page (int): The page number to calculate the index range for.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: The start and end indices for the given page and page size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """A class to handle pagination of data from a CSV file.

    Attributes:
        DATA_FILE (str): The path to the CSV file to read the data from.
        __dataset (List[List]): The data read from the CSV file, stored in memory.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server object.

        The dataset is initially set to None, and is loaded from the CSV file on demand.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Get the dataset from memory.

        If the dataset is not already loaded, it is loaded from the CSV file and stored in memory.

        Returns:
            List[List]: The dataset read from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page of data from the dataset.

        Args:
            page (int, optional): The page number to retrieve. Defaults to 1.
            page_size (int, optional): The number of items per page. Defaults to 10.

        Returns:
            List[List]: The page of data from the dataset.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]
