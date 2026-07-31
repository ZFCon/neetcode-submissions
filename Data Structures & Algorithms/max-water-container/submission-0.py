class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = float("-inf")
        n = len(heights)
        l, r = 0, n-1

        while l < r:
            water = min(heights[l], heights[r]) * (r-l)
            result = max(result, water)

            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1


        return result