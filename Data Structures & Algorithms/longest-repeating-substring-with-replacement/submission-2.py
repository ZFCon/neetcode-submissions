class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        results = 0
        memo = {} # keep track of characters count, make sure it does not exceed k
        l, r = 0, 0

        while r < len(s):
            # count the characters
            memo[s[r]] = memo.get(s[r], 0) + 1

            # current window
            window = r-l+1
            # the must used char
            top_char = max(memo.keys(), key=lambda x: memo[x])
            # the rest
            others = window - memo[top_char]

            # if the the others is more than the k we cut from behind
            while others > k:
                memo[s[l]] -= 1
                l += 1

                # current window
                window = r-l+1
                # the must used char
                top_char = max(memo.keys(), key=lambda x: memo[x])
                # the rest
                others = window - memo[top_char]

            results = max(results, window)

            r += 1

        return results