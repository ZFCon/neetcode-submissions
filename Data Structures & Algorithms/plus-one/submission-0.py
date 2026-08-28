from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # use join to convert to str
        joined_str = "".join(str(d) for d in digits)
        
        # then convert to int add 1
        incremented_num = int(joined_str) + 1
        
        # then convert to str and convert to list
        return [int(char) for char in str(incremented_num)]