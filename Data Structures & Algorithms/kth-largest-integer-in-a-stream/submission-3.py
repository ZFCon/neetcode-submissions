class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        inserted = False
        for i in range(len(self.nums)):
            if self.nums[i] >= val:
                self.nums.insert(i, val)
                inserted = True
                break

        if not inserted:
            self.nums.append(val)
        
        return self.nums[-self.k]
