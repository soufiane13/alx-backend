#!/usr/bin/env python3
"""Module for task 1.

This module contains a class that implements a FIFO caching system.
"""


from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class implementing a FIFO caching system.

    This class provides methods to store and retrieve items from a cache
    with a fixed size. The oldest items are discarded first (FIFO) when the
    cache is full.
    """

    def __init__(self):
        """Initialize the cache.

        The cache is initialized as an ordered dictionary with a maximum
        size set by the MAX_ITEMS constant from the BaseCaching class.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Store an item in the cache.

        If the key is None or the item is None, the method does nothing.
        Otherwise, the item is stored in the cache. If the cache is full,
        the oldest item is discarded first (FIFO) before adding the new
        item.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieve an item from the cache.

        If the key is None or the item does not exist in the cache, the
        method returns None.
        """
        return self.cache_data.get(key, None)
