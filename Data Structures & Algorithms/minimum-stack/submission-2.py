import heapq

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_value = float("inf")

    def push(self, val: int) -> None:
        self.min_value = min(val, self.min_value)
        self.stack.append((val, self.min_value))

    def pop(self) -> None:
        removed = self.stack.pop()
        self.min_value = self.stack[-1][1] if len(self.stack) else float("inf")
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
