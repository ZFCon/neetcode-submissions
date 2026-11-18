class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        result = float("inf"), ""
        memo = {char: t.count(char) for char in set(t)}
        l, r = 0, 0

        while r < len(s):
            # the head is in the important char then take
            if s[r] in memo:
                memo[s[r]] -= 1

            # valid window
            is_valid = not any(v > 0 for v in memo.values())

            while is_valid:
                # current window size
                window = r-l+1
                if window < result[0]:
                    result = window, s[l:r+1]

                # the tail is in the important char then take
                if s[l] in memo:
                    memo[s[l]] += 1
                l += 1

                is_valid = not any(v > 0 for v in memo.values())

            r += 1

        return result[1]