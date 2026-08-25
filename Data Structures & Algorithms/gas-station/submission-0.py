from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        # The Global Check
        if sum(gas) < sum(cost):
            return -1
            
        # Dictionary setup (kept exactly as you wrote it)
        stations = {i: {} for i in range(n)}
        prev = n-1
        for i in range(n):
            stations[prev]["next"] = i
            stations[i]["gas"] = gas[i]
            stations[i]["cost"] = cost[i]
            prev = i

        doomed = set()
        
        # Just iterate sequentially - no heap needed!
        for i in range(n):
            # 1. Prune stations we already proved will fail
            if i in doomed:
                continue
                
            mg = stations[i]["gas"] - stations[i]["cost"]

            # 2. Prune stations where we instantly crash
            if mg < 0:
                continue

            j = stations[i]["next"]
            while True:
                # Add every station we touch to the doomed list
                doomed.add(j)
                
                mg += stations[j]["gas"]

                if j == i:
                    return i
                elif mg < stations[j]["cost"]:
                    break
                else:
                    mg -= stations[j]["cost"]
                    j = stations[j]["next"]

        return -1