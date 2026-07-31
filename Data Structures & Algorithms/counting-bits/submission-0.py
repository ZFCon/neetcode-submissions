class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = []
        for i in range(n+1):
            counter.append(len("{:08b}".format(i).replace("0", "")))
        return counter