class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)

        while len(stones) > 1:
            stones[0] = abs(stones[0] - stones[1])
            del stones[1]
            stones.sort(reverse=True)


        return stones[0] if len(stones) else 0