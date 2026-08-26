from collections import Counter
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # create a counter for words (characters)
        counts = Counter(s)
        
        result = []
        
        # start at the begging
        # create a set of current characters
        current_chars = set()
        current_seen = Counter()
        size = 0
        
        for char in s:
            current_chars.add(char)
            current_seen[char] += 1
            size += 1
            
            # with each step you make sure you have covered the whole count of characters from the character set
            all_covered = True
            for c in current_chars:
                if current_seen[c] < counts[c]:
                    all_covered = False
                    break
                    
            # once this is correct you got your first partion and repeat
            if all_covered:
                result.append(size)
                # clear for the next partition
                current_chars.clear()
                current_seen.clear()
                size = 0
                
        return result