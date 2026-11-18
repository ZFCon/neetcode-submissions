class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        n = len(s)
        result = 0
        
        l, r = 0, 0
        while r < n:
            if s[r] in visited:
                l = max(visited[s[r]]+1, l)

            result = max(result, r-l+1) # 1-1+1 = 1
            visited[s[r]] = r # v{a: 0, b: 1}
            r += 1

        return result