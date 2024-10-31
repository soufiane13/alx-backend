#!/usr/bin/python3

from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    A class that inherits from BaseCaching and is a LFU caching system.

    It has the following methods:
        - put: Adds a key/value pair to the cache.
        - get: Retrieves a value from the cache.
        - _balance: Balances the cache by removing the least frequently used
            item if the cache is full.
    """

    def __init__(self):
        """
        Initializes the LFUCache instance.

        It calls the parent's __init__ method and initializes the following
        attributes:
            - __stats: A dictionary that maps keys to their frequency of usage.
            - __rlock: A RLock object that is used to synchronize access to the
                cache.
        """
        super().__init__()
        self.__stats = {}
        self.__rlock = RLock()

    def put(self, key, item):
        """
        Adds a key/value pair to the cache.

        If the cache is full, it removes the least frequently used item before
        adding the new key/value pair.

        Args:
            key (str): The key of the item to add.
            item (object): The item to add.
        """
        if key is not None and item is not None:
            keyOut = self._balance(key)
            with self.__rlock:
                self.cache_data.update({key: item})
            if keyOut is not None:
                print('DISCARD: {}'.format(keyOut))

    def get(self, key):
        """
        Retrieves a value from the cache.

        If the key is not in the cache, it returns None.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            object: The item associated with the key or None if the key is not
                in the cache.
        """
        with self.__rlock:
            value = self.cache_data.get(key, None)
            if key in self.__stats:
                self.__stats[key] += 1
        return value

    def _balance(self, keyIn):
        """
        Balances the cache by removing the least frequently used item if the
        cache is full.

        If the cache is full, it removes the least frequently used item and
        returns its key. Otherwise, it returns None.

        Args:
            keyIn (str): The key of the item that is being added to the cache.

        Returns:
            str: The key of the item that was removed or None if the cache is
                not full.
        """
        keyOut = None
        with self.__rlock:
            if keyIn not in self.__stats:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    keyOut = min(self.__stats, key=self.__stats.get)
                    self.cache_data.pop(keyOut)
                    self.__stats.pop(keyOut)
            self.__stats[keyIn] = self.__stats.get(keyIn, 0) + 1
        return keyOut
