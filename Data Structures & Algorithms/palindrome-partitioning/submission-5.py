from typing import List

class Solution:
    # FIX: Updated the helper to accept the full string and the two pointers.
    # We no longer need to pass a sliced copy of the string!
    def isValid(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        results = []

        def dfs(start: int, path: List[str]) -> None:
            if start == len(s):
                results.append(path.copy())
                return

            for i in range(start, len(s)):
                if self.isValid(s, start, i):
                    path.append(s[start:i+1])
                    dfs(i + 1, path)
                    path.pop()

        dfs(0, [])
        return results