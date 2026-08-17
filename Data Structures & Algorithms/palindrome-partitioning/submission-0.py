from typing import List

class Solution:
    def isValid(self, text: str) -> bool:
        # FIX: Replaced the list creation with string slicing. 
        # This does the exact same thing but is vastly faster!
        return text == text[::-1]

    def partition(self, s: str) -> List[List[str]]:
        results = []

        # FIX: Dropped the 'r' parameter. We only need one index ('start') 
        # to track where the current substring we are checking begins.
        def dfs(start: int, path: List[str]) -> None:
            # FIX: The base case is when our start index reaches the end of the string.
            # This means we successfully partitioned the whole string into palindromes.
            if start == len(s):
                results.append(path)
                return

            # FIX: Loop from 'start' to the end of the string.
            for i in range(start, len(s)):
                
                # FIX: Sliced from 'start' to 'i + 1'. 
                # In Python, slices are exclusive at the end, so i+1 includes the character at index i.
                current_substring = s[start:i+1]
                
                if self.isValid(current_substring):
                    # FIX: If it is a palindrome, we add it to the path and recursively 
                    # call dfs starting from the very next character (i + 1).
                    dfs(i + 1, path + [current_substring])
                    
                    # FIX: Removed the second dfs() call and the 'break'. 
                    # The 'for' loop will automatically move 'i' forward to try longer 
                    # slices, so we don't need to manually force it to explore other branches!

        # FIX: Start the DFS at index 0 with an empty path.
        dfs(0, [])
        return results