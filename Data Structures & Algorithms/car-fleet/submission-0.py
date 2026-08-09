class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0

        stack = [(p, s) for p, s in zip(position, speed)]
        stack.sort(key=lambda x: x[0])
        n = len(stack)
        result = 1
        bt = (target - stack[-1][0]) / stack[-1][1]

        for i in range(n-1, -1, -1):
            curr_bt = (target - stack[i][0]) / stack[i][1]

            if curr_bt <= bt:
                continue
            else:
                bt = curr_bt
                result += 1

        return result