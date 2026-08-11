class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        result = 0

        # --- FORWARD PASS ---
        l, r = 0, 0
        ga = 0
        while r < n:
            # REMOVED: if l == 0: l += 1
            if l != r:
                if height[l] <= height[r]:
                    result += (min(height[l], height[r]) * (r - l - 1)) - ga
                    l = r
                    ga = 0
                elif height[l] > height[r]:
                    ga += height[r]
            r += 1

        # --- BACKWARD PASS ---
        r, l = n - 1, n - 1
        ga = 0
        while l >= 0:
            # REMOVED: if r == n - 1: r -= 1
            if r != l:
                # If the anchor (r) is strictly less than the explorer (l)
                if height[r] < height[l]:
                    # The max(..., 0) shield is no longer strictly necessary, 
                    # but safe to keep.
                    result += max((min(height[r], height[l]) * (r - l - 1)) - ga, 0)
                    r = l
                    ga = 0
                    
                # If the anchor (r) is taller OR EQUAL to the explorer (l)
                elif height[r] >= height[l]:
                    ga += height[l]
            l -= 1

        return result