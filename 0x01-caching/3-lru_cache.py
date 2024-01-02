#!/usr/bin/env python3
"""
Implements LRU caching algorithm
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    a class that implements a LIFO cache algorithm
    """
    lru_mru = []

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

            if key in self.lru_mru:
                self.lru_mru.append(key)
                self.lru_mru.remove(key)
            else:
                self.lru_mru.append(key)

            if len(self.lru_mru) > self.MAX_ITEMS:
                del self.cache_data[self.lru_mru[0]]
                print(f'DISCARD: {self.lru_mru[0]}')
                self.lru_mru.pop(0)

    def get(self, key):
        """gets an item from cache
        """
        item = self.cache_data.get(key)

        if item:
            self.lru_mru.append(key)
            self.lru_mru.remove(key)

        return item
