import urllib.parse
from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Explicitly handle the empty list to avoid the split() bug
        if strs == []:
            return "EMPTY_LIST"
            
        return ",".join(urllib.parse.quote(s) for s in strs)

    def decode(self, s: str) -> List[str]:
        # Catch the empty list edge case
        if s == "EMPTY_LIST":
            return []
            
        return [urllib.parse.unquote(char) for char in s.split(",")]