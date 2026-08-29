from functools import cache
class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0 or n == 0:
            return 1
        if n < 0:
            x = 1 / x
        n = abs(n)

        base = x if n % 2 else 1
        return self.myPow(x, n//2) * self.myPow(x, n//2) * base