class LRUCache:
    def __init__(self, capacity: int):
        self.capacity  = capacity
        self.data = {}
        self.used = {}
        self.time = 0       # FIX 1: Add a global time counter

    def use(self, key: int) -> None:
        if key not in self.used:
            self.capacity -= 1
            
        # FIX 2: Change <= to <. 
        # If capacity is 0, the cache is exactly full (which is fine). 
        # We only want to evict if we go BELOW 0 (meaning we overflowed).
        if self.capacity < 0:
            min_key = min(self.used.keys(), key=lambda x: self.used[x])
            del self.data[min_key]
            del self.used[min_key]
            self.capacity += 1

        # FIX 3: Track the "time" it was used, rather than counting frequency.
        # Now, min() will correctly find the OLDEST time, not the lowest count!
        self.time += 1
        self.used[key] = self.time

    def get(self, key: int) -> int:
        if key in self.data:
            self.use(key)
        
        result = self.data.get(key, -1)
        return result

    def put(self, key: int, value: int) -> None:
        self.data[key] = value
        self.use(key)