from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def dfs(i1, i2):
            # Base Case: If we reach the end of the pattern, 
            # we must also be at the end of the string for a valid match.
            if i2 >= len(p):
                return i1 >= len(s)
                
            # Check if the current characters match (handling out of bounds and '.')
            match = i1 < len(s) and (s[i1] == p[i2] or p[i2] == '.')
            
            # Look ahead: Is the next character in the pattern a '*'?
            if i2 + 1 < len(p) and p[i2 + 1] == '*':
                # Path 1: Don't use the '*' (skip the char and the '*')
                # Path 2: Use the '*' (consume 1 char from 's', keep 'p' at the same spot)
                return dfs(i1, i2 + 2) or (match and dfs(i1 + 1, i2))
                
            # Standard character match without a trailing '*'
            if match:
                return dfs(i1 + 1, i2 + 1)
                
            # If they don't match and there is no '*', this path fails
            return False
            
        return dfs(0, 0)