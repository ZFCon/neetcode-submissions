class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i, n = 0, len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:  # ends before the new one starts
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:  # overlaps the new one
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        result.extend(intervals[i:])  # starts after the new one ends
        return result
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        def best_from_left_ends(segs):
            segs.sort()  # by l
            n = len(segs)
            pre = [0] * (n + 1)  # pre[i] = coins in the full segments before i
            for i, (l, r, c) in enumerate(segs):
                pre[i + 1] = pre[i] + (r - l + 1) * c

            best = 0
            j = 0
            for i in range(n):
                lk = segs[i][0] + k - 1  # last bag of the window that starts at l
                while j < n and segs[j][1] <= lk:  # segment j fully inside
                    j += 1
                total = pre[j] - pre[i]
                if j < n and segs[j][0] <= lk:  # segment j only partly inside
                    total += (lk - segs[j][0] + 1) * segs[j][2]
                best = max(best, total)
            return best

        flipped = [[-r, -l, c] for l, r, c in coins]
        return max(best_from_left_ends(coins), best_from_left_ends(flipped))