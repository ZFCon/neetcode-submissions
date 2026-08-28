from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Create a DFS function that takes i1 and i2
        @cache
        def dfs(i1, i2):
            # if we reached the end of both return the 0 so we can count the amount of operations
            if i1 == len(word1) and i2 == len(word2):
                return 0
                
            # (Handling if we reach the end of one string before the other)
            if i1 == len(word1):
                return len(word2) - i2  # Need to insert the rest of word2
            if i2 == len(word2):
                return len(word1) - i1  # Need to delete the rest of word1
                
            # first condition if both indexes equal the same character
            if word1[i1] == word2[i2]:
                # we simply skip them without counting operation
                return dfs(i1 + 1, i2 + 1)
                
            # if the current character does not equal then we we create 3 dfs
            # insert the character we need (advance in word2, stay in word1)
            insert = dfs(i1, i2 + 1)
            # delete the character that don't equal (advance in word1, stay in word2)
            delete = dfs(i1 + 1, i2)
            # or replace (advance in both)
            replace = dfs(i1 + 1, i2 + 1)
            
            # at the end get the minimum results (and add 1 for the current operation)
            return 1 + min(insert, delete, replace)
            
        return dfs(0, 0)