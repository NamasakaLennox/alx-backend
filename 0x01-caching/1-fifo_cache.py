#!/usr/bin/env python3
"""
implements a FIFO cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    implements a fifo caching algorithm
    """
    def __init__(self):
        """
        constructor class for the method
        """
        super().__init__()

    def put(self, key, item):
        """
        adds an item to the cache dictionary
        """
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                d_key = list(self.cache_data.keys())[0]
                del self.cache_data[d_key]
                print(f'DISCARD: {d_key}')

    def get(self, key):
        """
        gets a value from the dictionary
        """
        return self.cache_data.get(key)
