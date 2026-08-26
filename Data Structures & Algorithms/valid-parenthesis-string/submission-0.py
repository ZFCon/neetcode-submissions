class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        
        def dfs(i, open_count):
            # If at any point we have more close than open, it's invalid
            if open_count < 0:
                return False
                
            # If we reached the end of the string, check if all opens are closed
            if i == len(s):
                return open_count == 0
                
            if (i, open_count) in memo:
                return memo[(i, open_count)]
                
            if s[i] == '(':
                res = dfs(i + 1, open_count + 1)
            elif s[i] == ')':
                res = dfs(i + 1, open_count - 1)
            else:
                # s[i] == '*'
                # Branch 1: put it as open '('
                # Branch 2: put it as close ')'
                # Branch 3: dismiss it (empty string)
                # The 'or' operator short-circuits: it returns True immediately if one branch works 
                # and ends the rest, exactly as requested.
                res = (dfs(i + 1, open_count + 1) or 
                       dfs(i + 1, open_count - 1) or 
                       dfs(i + 1, open_count))
                       
            memo[(i, open_count)] = res
            return res
            
        return dfs(0, 0)