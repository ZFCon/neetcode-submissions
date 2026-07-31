from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        if not amount:
            return 0
        result = float("inf")
        q = deque([[coin, 1] for coin in coins])
        seen = set()

        while q:
            sum_amount, counter = q.popleft()
            if sum_amount == amount:
                result = min(result, counter)
                return result
            if sum_amount in seen or sum_amount > amount:
                continue

            for coin in coins:
                q.append([sum_amount+coin, counter+1])

            seen.add(sum_amount)


        return result if result != float("inf") else -1