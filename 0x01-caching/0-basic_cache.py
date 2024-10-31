#!/usr/bin/env python3

'''Task 0: Basic dictionary
'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Defines a basic caching class that implements
    the put and get methods using a dictionary
    """

    def put(self, key, item):
        """
        Stores an item in the cache with the given
        key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache with the
        given key
        """
        return self.cache_data.get(key, None)
