import bisect

class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
            
        # bisect automatically compares the first element of the tuple (timestamp)
        bisect.insort(self.data[key], (timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        data = self.data.get(key, [])
        n = len(data)
        if data and data[-1][0] <= timestamp:
            return data[-1][1]
        if not data:
            return ""

        l, r = 0, n-1

        while l <= r:
            mid = (l+r) // 2

            if data[mid][0] == timestamp:
                return data[mid][1]
            if data[mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid - 1

        if data[mid][0] <= timestamp:
            return data[mid][1]
        elif 0 < mid and data[mid-1][0] <= timestamp:
            return data[mid-1][1]
        return ""




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)