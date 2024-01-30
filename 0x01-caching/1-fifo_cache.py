#!/usr/bin/env python3
'''FIFO cahcing'''


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''fifo class'''
    
    def __init__(self):
        '''init func'''
        super().__init__()
        
    def put(self, key, item):
        '''func2'''
        if key is None or item is None:
            pass
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = next(iter(self.cache_data))
            del self.cache_data[discarded_key]
            print("DISCARD: {}".format(discarded_key))

        self.cache_data[key] = item

    def get(self,key):
        '''get func'''
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data.get(key)
