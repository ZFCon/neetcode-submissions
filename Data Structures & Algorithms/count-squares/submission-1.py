from collections import defaultdict
from typing import List

class CountSquares:

    def __init__(self):
        self.data_count = defaultdict(int)
        self.data = []

    def add(self, point: List[int]) -> None:
        self.data_count[tuple(point)] += 1
        self.data.append(tuple(point))

    def count(self, point: List[int]) -> int:
        result = 0
        px, py = point

        for x, y in self.data:
            if abs(x-px) != abs(y-py) or x == px or y == py:
                continue
            
            result += self.data_count[(x, py)] * self.data_count[(px, y)]

        return result
        