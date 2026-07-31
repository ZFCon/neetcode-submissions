class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        compos = set()
        nums = set([num for num in nums if num <= target])
        q = [[num] for num in nums]

        while q:
            compo_nums = q.pop()
            sum_nums = sum(compo_nums)
            if sum_nums == target:
                compos.add(tuple(sorted(compo_nums)))
                continue
            if sum_nums > target:
                continue

            for num in nums:
                if sum_nums + num <= target:
                    q.append(compo_nums + [num])

        return [list(compo) for compo in compos]