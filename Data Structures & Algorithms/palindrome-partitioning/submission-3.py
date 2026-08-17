from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        
        # FIX: Initialize the memoization dictionary (our notepad)
        memo = {}

        # FIX: Moved isValid inside partition so we don't have to constantly pass 's' and 'memo' to it.
        def isValid(left: int, right: int) -> bool:
            # FIX: Step 1 - Check the notepad! If we already know the answer, return it instantly.
            if (left, right) in memo:
                return memo[(left, right)]
            
            # We must save the original pointers because the while loop modifies 'left' and 'right'
            orig_left, orig_right = left, right
            
            while left < right:
                if s[left] != s[right]:
                    # FIX: Step 2 - Save the failure to the notepad before returning
                    memo[(orig_left, orig_right)] = False
                    return False
                left += 1
                right -= 1
            
            # FIX: Step 3 - Save the success to the notepad before returning
            memo[(orig_left, orig_right)] = True
            return True

        def dfs(start: int, path: List[str]) -> None:
            if start == len(s):
                # Perfect! You correctly used path.copy() to save the snapshot
                results.append(path.copy())
                return

            for i in range(start, len(s)):
                # FIX: Call the new nested isValid function with just the pointers
                if isValid(start, i):
                    
                    # Perfect! The Choose -> Explore -> Un-choose memory pattern is flawless
                    path.append(s[start:i+1])
                    dfs(i + 1, path)
                    path.pop()

        dfs(0, [])
        return results