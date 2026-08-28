class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
            
        # create a memo that holds the 3 index result
        memo = {}
            
        def dfs(i1, i2, i3):
            if i3 == len(s3):
                return True
                
            # If we've seen this exact state before, return the saved result
            if (i1, i2, i3) in memo:
                return memo[(i1, i2, i3)]
                
            if i1 < len(s1) and s1[i1] == s3[i3]:
                if dfs(i1 + 1, i2, i3 + 1):
                    memo[(i1, i2, i3)] = True
                    return True
                    
            if i2 < len(s2) and s2[i2] == s3[i3]:
                if dfs(i1, i2 + 1, i3 + 1):
                    memo[(i1, i2, i3)] = True
                    return True
                    
            # If neither path worked, save False to the memo
            memo[(i1, i2, i3)] = False
            return False
            
        return dfs(0, 0, 0)