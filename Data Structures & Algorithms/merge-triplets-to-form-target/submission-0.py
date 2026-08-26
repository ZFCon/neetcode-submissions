import heapq
from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        heap = []
        
        # In the heap, we sort the data using how many numbers from target are there
        for i, triplet in enumerate(triplets):
            # CRITICAL FIX: Skip triplets that have ANY value greater than the target.
            # If we combine them, the max() operation will permanently overshoot the target.
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
                
            matches = 0
            if triplet[0] == target[0]:
                matches += 1
            if triplet[1] == target[1]:
                matches += 1
            if triplet[2] == target[2]:
                matches += 1
                
            # Use -matches to prioritize triplets with the most target numbers first
            heapq.heappush(heap, (-matches, i, triplet))
            
        if not heap:
            return False
            
        # Pop the first object to initialize our current combined triplet
        _, _, first_triplet = heapq.heappop(heap)
        current = list(first_triplet)
        
        if current == target:
            return True
            
        # Pop object after object and use the operation to combine
        while heap:
            _, _, next_triplet = heapq.heappop(heap)
            
            current[0] = max(current[0], next_triplet[0])
            current[1] = max(current[1], next_triplet[1])
            current[2] = max(current[2], next_triplet[2])
            
            # If we finally got the target return true
            if current == target:
                return True
                
        # Return false if the heap is empty and we didn't get the target
        return False