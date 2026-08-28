class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # create a memo that take i1 and i2
        memo = {}
        
        # create dfs that take i1 and i2
        def dfs(i1, i2):
            # if we reached the end you count one (we successfully matched all of t)
            if i2 == len(t):
                return 1
                
            # if we reach the end of s but haven't finished t, we can't form the word
            if i1 == len(s):
                return 0
                
            # check the memo before doing any calculations
            if (i1, i2) in memo:
                return memo[(i1, i2)]
                
            # if the character at i1 in s equals the character at i2 in t
            if s[i1] == t[i2]:
                # then either take it or skip it
                take = dfs(i1 + 1, i2 + 1)
                skip = dfs(i1 + 1, i2)
                memo[(i1, i2)] = take + skip
            else:
                # if not equal we could only skip it
                memo[(i1, i2)] = dfs(i1 + 1, i2)
                
            return memo[(i1, i2)]
                
        return dfs(0, 0)