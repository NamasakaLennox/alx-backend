#!/usr/bin/env python3
"""
Implements a basic dictionary as a cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    implements a dictionary for caching without a limit
    """
    def __init__(self):
        """
        constructor method for the class
        """
        super().__init__()

    def put(self, key, item):
        """
        assign a value to the dictionary
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        gets a value from the dictionary
        """
        return self.cache_data.get(key)
