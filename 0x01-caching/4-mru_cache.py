#!/usr/bin/env python3

"""
A class that inherits from BaseCaching and is a most recently used (MRU)
cache system.
"""

from collections import OrderedDict

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching and is a most recently used
    (MRU) cache system.
    """

    def __init__(self):
        """
        Initialize the MRUCache class by calling the parent class's
        __init__() method and creating an empty OrderedDict that will store
        the cache data.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add a key-value pair to the cache data if the key is not already in
        the cache data. If the cache data is full, remove the most recently
        used item (the last item in the OrderedDict) and add the new
        key-value pair. If the key is already in the cache data, update the
        value associated with the key.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru_key)

            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value associated with the given key if it exists in the
        cache data. If the key does not exist, return None.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
