class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        previous = 1
        for num in nums:
            prefix.append(num*previous)
            previous = num*previous

        postfix = []
        previous = 1
        for num in reversed(nums):
            postfix.insert(0, num*previous)
            previous = num*previous

        results = []
        n = len(nums)
        for i in range(n):
            pre = 1
            post = 1

            if i > 0:
                pre = prefix[i-1]
            
            if i < n-1:
                post = postfix[i+1]

            results.append(pre*post)

        return results
