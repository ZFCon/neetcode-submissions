class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        n1 = len(text1)
        n2 = len(text2)
        
        def dfs(p1, p2) -> int:
            if p1 >= n1 or p2 >= n2:
                return 0

            if (p1, p2) in memo:
                return memo[(p1, p2)]

            if text1[p1] == text2[p2]:
                ans = 1 + dfs(p1+1, p2+1)
            else:
                ans = max(dfs(p1+1, p2), dfs(p1, p2+1))

            memo[(p1, p2)] = ans

            return ans

        return dfs(0, 0)