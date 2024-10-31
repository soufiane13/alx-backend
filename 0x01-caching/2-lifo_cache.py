#!/usr/bin/env python3
"""Task 2: LIFO Caching.

This module implements a basic LIFO (Last In First Out) cache using an ordered
dictionary. The cache is bounded to a maximum number of items, and when the
maximum number is exceeded, the last item added to the cache is discarded.

"""

from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Implements a LIFO (Last In First Out) cache using an ordered dictionary.

    The cache is bounded to a maximum number of items, and when the maximum
    number is exceeded, the last item added to the cache is discarded.

    """

    def __init__(self):
        """Initializes the cache.

        This method initializes the cache by calling the parent's __init__
        method and initializing the cache data structure as an ordered
        dictionary.

        """

        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item to the cache.

        This method adds an item to the cache. If the key is not in the cache
        and the cache is full, the last item added to the cache is discarded.

        Parameters
        ----------
        key : str
            The key for the item to be added to the cache.
        item :
            The item to be added to the cache.

        """

        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)
