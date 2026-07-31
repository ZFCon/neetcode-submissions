class Solution:
    def hammingWeight(self, n: int) -> int:
        return len("{:b}".format(n).replace("0", ""))