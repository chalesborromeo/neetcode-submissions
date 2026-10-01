class LRUCache:

    '''

    design problem?
    we have a cache that will store values, we need get value based on a key value

    use hashmap to instantly look at every value at o(1)


    '''

    def __init__(self, capacity: int):
        
        # we setup an empty cache and remember the size limit 
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        
        # cache miss if key/value isn't in there return -1
        if key not in self.cache:
            return -1
        
                
        # cache hits, reading a key/value counts as using. mark this key as recently used
        # before returning value.
        self.cache.move_to_end(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
 
        # assigning to an existing key updates the value but does not
        # change its position. 
        # for an existing key, you need to call move_to_end. 
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)