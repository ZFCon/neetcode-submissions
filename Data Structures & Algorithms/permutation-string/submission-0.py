class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        s1 = "".join(sorted(s1))

        l, r = 0, n1-1
        while r < n2:
            if s1 == "".join(sorted(s2[l:r+1])):
                return True
            l += 1
            r += 1

        return False