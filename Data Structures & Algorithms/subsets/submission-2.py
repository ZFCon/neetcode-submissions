class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = set()

        def dfs(current: List[int], numbers: List[int]) -> None:
            current.sort()
            
            # Convert list to a tuple so it can be hashed and stored in the set
            current_tuple = tuple(current)

            if not len(numbers):
                if current_tuple not in results:
                    results.add(current_tuple)
                return
            
            current_tuple not in results

            if current_tuple not in results:
                results.add(current_tuple) # Changed .append() to .add() for sets
            else:
                return

            for i in range(len(numbers)):
                dfs(current+[numbers[i]], [numbers[index] for index in range(len(numbers)) if index != i])
        

        dfs([], nums)
        # Convert the tuples inside the set back into lists for the final output
        return [list(r) for r in results]