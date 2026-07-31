class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        # Pre-count all substrings of length 1
        counter = n 

        for i in range(n):
            # Start j at i + 2 so the minimum substring length is 2
            for j in range(i + 2, n + 1):
                sen = s[i:j]
                rev = s[i:j][::-1]

                if rev == sen:
                    counter += 1

        return counter