class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        
        # FIX: You don't need to put len(nums) inside a list! As long as you only 
        # READ the variable inside dfs() and don't reassign it, a standard integer works.
        n = len(nums) 
        visited = set()

        def dfs(path: List[int]) -> None:
            # FIX: Updated to use the standard integer 'n'
            if len(path) == n:
                results.append(path.copy())
                return
    
            # FIX: Loop directly through the numbers instead of using range(n)
            for num in nums:
                # FIX: Check if the NUMBER is in visited, rather than the index
                if num not in visited:
                    visited.add(num)
                    
                    # FIX: Append the actual number to our path
                    path.append(num)
                    
                    dfs(path)
                    
                    path.pop()
                    visited.remove(num)

        dfs([])
        
        # FIX: Because our path is now filled with actual numbers instead of indices, 
        # we can just return 'results' directly! The complex list comprehension is gone.
        return results