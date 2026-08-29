from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def dfs(i1, i2):
            # Both pointers successfully reached before the start (fully consumed)
            if i1 < 0 and i2 < 0:
                return True
            
            # Pattern ran out but string didn't
            if i2 < 0:
                return False

            # 1. If current char is '*' (Your branching logic)
            if p[i2] == '*':
                # Path A: Skip pattern (zero occurrences)
                # We skip the '*' AND the character it modifies, so i2 - 2
                path1 = dfs(i1, i2 - 2)
                
                # Path B: Consume one string character (if it matches the modified char)
                # The character being modified is safely at p[i2 - 1]
                path2 = False
                if i1 >= 0 and (s[i1] == p[i2 - 1] or p[i2 - 1] == '.'):
                    # Move string pointer back, but keep pattern pointer on '*'
                    path2 = dfs(i1 - 1, i2)
                    
                # Note: Path C (skip both) is naturally handled by Path B looping once 
                # and then taking Path A on the next recursion.
                return path1 or path2

            # String ran out but pattern is still asking for a strict letter/dot
            # (Moved BELOW the '*' check, because 'a*' can validly match an empty string)
            if i1 < 0:
                return False

            # 2. If current char is '.' skip index in both
            if p[i2] == '.':
                return dfs(i1 - 1, i2 - 1)

            # 3. If normal characters match, move both backward
            if s[i1] == p[i2]:
                return dfs(i1 - 1, i2 - 1)

            # 4. If i1 != i2, return False
            return False

        # Start from the very last index of both strings
        return dfs(len(s) - 1, len(p) - 1)