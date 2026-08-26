class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 10:24am

        if len(hand) % groupSize:
            return False
        
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        
        heap = list(count.keys())
        heapq.heapify(heap)

        while heap:
            if count[heap[0]] == 0:
                heapq.heappop(heap)
                continue
            
            n = heap[0]
            for i in range(n, n + groupSize):
                if count.get(i, 0) == 0:
                    return False
                count[i] -= 1
        
        return True