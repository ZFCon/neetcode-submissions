import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        
        for num in nums:
            # Find the index where 'num' should be inserted to maintain sorted order
            i = bisect.bisect_left(sub, num)
            
            # If 'num' is larger than any element in sub, it extends the longest sequence
            if i == len(sub):
                sub.append(num)
            # Otherwise, replace the first element that is >= 'num'
            else:
                sub[i] = num
                
        return len(sub)