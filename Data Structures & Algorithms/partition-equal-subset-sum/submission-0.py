from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        whole = sum(nums)
        
        # Add this check: If the sum is odd, it's impossible to partition equally
        if whole % 2 != 0:
            return False
            
        half = whole // 2
        nums.sort()
        n = len(nums)

        for i in range(n):
            current_sum = nums[i]

            j = i + 1
            used = {i} 
            
            while current_sum < half:
                target = half - current_sum
                found_idx = -1
                
                for k in range(n - 1, -1, -1):
                    if k not in used and nums[k] <= target:
                        found_idx = k
                        break
                
                if found_idx == -1:
                    break
                    
                current_sum += nums[found_idx]
                used.add(found_idx)

            if current_sum == half:
                return True

        return False