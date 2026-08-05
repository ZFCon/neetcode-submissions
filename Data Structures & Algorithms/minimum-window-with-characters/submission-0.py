from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        countT, window = Counter(t), {}
        have, need = 0, len(countT)

        result, resultLen = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < resultLen:
                    result = [l, r]
                    resultLen = r-l+1

                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1


        l, r = result
        return s[l:r+1] if resultLen != float("inf") else ""