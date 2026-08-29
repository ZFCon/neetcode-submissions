from collections import defaultdict
from typing import List

class CountSquares:

    def __init__(self):
        # data[x][y] stores the frequency of the point
        self.data = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point
        self.data[x][y] += 1

    def count(self, point: List[int]) -> int:
        qx, qy = point
        total_squares = 0
        
        # Create a static copy of the keys to prevent RuntimeError if the dictionary changes size elsewhere
        x_coords = list(self.data.keys())

        # Loop through existing x-coordinates safely using a list copy
        for x in x_coords:
            if x == qx:
                continue
            length = abs(x - qx)
            
            # Check all 4 possible directions (quadrants relative to query point)
            for dy_sign in [-1, 1]:
                y = qy + (length * dy_sign)
                if y in self.data[x]:
                    c1_freq = self.data[qx][y]
                    c2_freq = self.data[x][qy]
                    c3_freq = self.data[x][y]
                    
                    if c1_freq > 0 and c2_freq > 0 and c3_freq > 0:
                        total_squares += c1_freq * c2_freq * c3_freq
                    
        return total_squares