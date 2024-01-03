#!/usr/bin/env python3
"""
Implements LFU caching algorithm
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    a class that implements a LFU cache algorithm
    """
    lfu = {}

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

            if key in self.lfu.keys():
                temp = self.lfu[key]
                del self.lfu[key]
                self.lfu[key] = temp + 1
            else:
                self.lfu[key] = 0

            if len(self.lfu) > self.MAX_ITEMS:
                keys = list(self.lfu.keys())[:-1]
                values = list(self.lfu.values())[:-1]
                index_dkey = values.index(min(values))
                d_key = keys[index_dkey]
                print(f'DISCARD: {d_key}')
                del self.lfu[d_key]
                del self.cache_data[d_key]

    def get(self, key):
        """gets an item from cache
        """
        item = self.cache_data.get(key)

        if item:
            temp = self.lfu[key]
            del self.lfu[key]
            self.lfu[key] = temp + 1

        return item
