from functools import cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
            
        @cache
        def dfs(i1, i2):
            # If we matched all of t, return 1
            if i2 == len(t):
                return 1
                
            # If remaining characters in s are fewer than remaining in t, impossible
            if len(s) - i1 < len(t) - i2:
                return 0
                
            # If we reach the end of s but haven't finished t
            if i1 == len(s):
                return 0
                
            # If characters match, take or skip
            if s[i1] == t[i2]:
                return dfs(i1 + 1, i2 + 1) + dfs(i1 + 1, i2)
            else:
                # If not equal, only skip
                return dfs(i1 + 1, i2)
                
        return dfs(0, 0)