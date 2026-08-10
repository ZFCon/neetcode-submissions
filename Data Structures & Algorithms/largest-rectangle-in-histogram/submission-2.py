from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = []  # stores (index, height)

        for i, h in enumerate(heights):
            start = i

            # When we see a shorter bar, resolve the taller bars in the stack
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Use the POPPED height, not 'h'
                result = max(result, height * (i - index))
                start = index

            stack.append((start, h))

        # Resolve the bars that extend to the very end of the array
        for i, h in stack:
            # Width is the full length minus the starting index
            result = max(result, h * (len(heights) - i))

        return result