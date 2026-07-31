class Solution:
    def reverseBits(self, n: int) -> int:
        bit_string = "{:032b}".format(n)
        return int(bit_string[::-1], 2)
