import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        xheap = [-value for value in counter.values()]
        heapq.heapify(xheap)

        q = deque()
        time = 0
        while xheap or q:
            time += 1
            if xheap:
                c = heapq.heappop(xheap) + 1
                if c:
                    q.append((time+n, c))
            if q and q[0][0] == time:
                heapq.heappush(xheap, q.popleft()[1])

        return time
                

