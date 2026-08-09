class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        dp = [0] * n

        for i in range(n-2, -1, -1):

            counter = 0
            for j in range(i+1, n):
                counter += 1
                if temperatures[i] < temperatures[j]:
                    dp[i] = counter
                    break
                elif temperatures[i] == temperatures[j]:
                    dp[i] = counter + dp[j] if dp[j] != 0 else 0
                    break
                elif temperatures[i] > temperatures[j] and temperatures[j] == 0:
                    dp[i] = 0
                    break

        return dp