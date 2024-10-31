#!/usr/bin/python3
"""
Module 3-lru_cache.py
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Class LRUCache that inherits from BaseCaching and is a caching system

    Attributes:
        cache_data (dict): a dictionary to store data
        keys (list): a list of keys in the cache
    """
    def __init__(self):
        """
        Initialize the cache
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Add or update an item in the cache

        If the cache is full and the key is not in the cache, remove the oldest
        item from the cache to make room for the new item.

        Args:
            key (str): the key to add or update
            item (object): the value to add or update
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                    and key not in self.keys:
                del_key = self.keys.pop(0)
                del self.cache_data[del_key]
                print("DISCARD: {}".format(del_key))
            if key in self.keys:
                self.keys.remove(key)
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache

        If the key is in the cache, move it to the end of the list to mark it as
        most recently used.

        Args:
            key (str): the key to retrieve

        Returns:
            object: the value associated with the key
        """
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
        value = self.cache_data.get(key)
        return value
