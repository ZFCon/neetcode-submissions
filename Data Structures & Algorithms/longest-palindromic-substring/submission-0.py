class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        result = ""
        
        def dfs(i: int, j: int) -> str:
            if i < 0 or j >= n or s[i] != s[j]:
                return s[i + 1:j]

            return dfs(i-1, j+1)

        for i in range(n):
            result = max(result, dfs(i, i), dfs(i, i+1), key=len)

        return result