class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        finder = {
            "}": "{",
            "]": "[",
            ")": "(",
        }
        q = []
        for char in s:
            if char in finder.values():
                q.append(char)
            else:
                if not len(q):
                    return False
                ender = q.pop()
                if finder[char] != ender:
                    return False
        
        return True if not len(q) else False