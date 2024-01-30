#!/usr/bin/env python3
'''FIFO caching'''

BaseCaching = __import__('base_caching').BaseCaching

class FIFOCache(BaseCaching):
    '''FIFO class'''

    def __init__(self):
        '''Init function'''
        super().__init__()

    def put(self, key, item):
        '''Put function'''
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key  = next(iter(self.cache_data))
            del self.cache_data[discarded_key]
            print("DISCARD: {}".format(discarded_key))

        self.cache_data[key] = item

    def get(self, key):
        '''get func'''
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)

