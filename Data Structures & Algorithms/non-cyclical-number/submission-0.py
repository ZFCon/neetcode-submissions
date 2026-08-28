class Solution:
    def isHappy(self, n: int) -> bool:
        # Check base case first just in case
        if n == 1:
            return True
            
        visited = set()
        
        # loop while the current number not in visited
        while n not in visited:
            visited.add(n)
            
            # inside the loop you do the calculation
            next_num = 0
            while n > 0:
                digit = n % 10
                next_num += digit ** 2
                n //= 10
                
            # and equal the number
            n = next_num
            
            # until if it equal 1 return true
            if n == 1:
                return True
                
        # if it's in visited break (while loop exits naturally) and return False
        return False