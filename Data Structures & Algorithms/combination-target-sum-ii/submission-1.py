import bisect
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # FIX: Corrected typo 'canadidates' to 'candidates' so we actually use the filtered list.
        candidates = [candidate for candidate in candidates if candidate <= target]
        candidates.sort()
        results = []
        
        # FIX: Added a visited set to keep track of paths we've already explored
        visited = set()

        def dfs(index: int, path: List[int]) -> None:
            # FIX: Convert the list to a tuple so it can be hashed and checked in the set
            path_tuple = tuple(path)
            
            # FIX: If we have already explored this exact path, skip it entirely!
            if path_tuple in visited:
                return
                
            # FIX: Mark this path as visited so we don't explore it again
            visited.add(path_tuple)

            if sum(path) == target:
                # FIX: Removed the 'if path not in results' check. 
                # The visited set already guarantees we won't reach here with a duplicate!
                results.append(path)
                return
            elif sum(path) > target:
                return

            for i in range(index, len(candidates)):
                # FIX: Because we sorted 'candidates' at the beginning, we are guaranteed 
                # that we are adding numbers in ascending order. We don't need to use 
                # bisect.insort(), we can just do a normal list append/addition!
                new_path = path + [candidates[i]]
                dfs(i+1, new_path)

        dfs(0, [])
        return results