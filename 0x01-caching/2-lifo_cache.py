#!/usr/bin/env python3
"""
Implements LIFO caching algorithm
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    a class that implements a LIFO cache algorithm
    """
    _last = None

    def __init__(self):
        """
        constructor method for the lifo class
        """
        super().__init__()

    def put(self, key, item):
        """
        adds an element to the cache
        """
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                del self.cache_data[self._last]
                print(f'DISCARD: {self._last}')

            self._last = key

    def get(self, key):
        """gets an item from cache
        """
        return self.cache_data.get(key)
