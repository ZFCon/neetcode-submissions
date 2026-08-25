class Solution:
    def jump(self, nums: List[int]) -> int:
        q = deque([[0, 0]])
        n = len(nums)
        mim = {}

        while q:
            i, jumps = q.popleft()

            if i >= n-1:
                return jumps
            if i in mim and mim[i] <= jumps:
                continue

            mim[i] = jumps

            for j in range(nums[i], -1, -1):
                if i+j <= n-1:
                    q.append([i+j, jumps+1])
                else:
                    return jumps+1

        return -1