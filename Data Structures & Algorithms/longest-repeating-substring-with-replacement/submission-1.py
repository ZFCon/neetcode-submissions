class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        n = len(s)
        
        l = 0
        counts = {}
        max_f = 0 # Tracks the highest count of a single character in the window
        
        for r in range(n):
            counts[s[r]] = counts.get(s[r], 0) + 1
            max_f = max(max_f, counts[s[r]])

            while (r - l + 1 - max_f) > k:
                counts[s[l]] -= 1
                l += 1

            result = max(result, r-l+1)


        return result