class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xffffffff
        MAX = 0x7fffffff

        x = a & MASK
        y = b & MASK

        while y != 0:
            carry = (x & y) << 1
            x = x ^ y
            y = carry & MASK


        return x if x <= MAX else ~(x ^ MASK)