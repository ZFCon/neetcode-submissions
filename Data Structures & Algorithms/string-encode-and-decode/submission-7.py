class Solution:
    def encode(self, strs: List[str]) -> str:
        text = ""
        
        for word in strs:
            text += f"{len(word)}#{word}"

        return text
    def decode(self, s: str) -> List[str]:
        n = len(s)
        results = []

        i = 0
        while i < n:
            j = i+1
            while j < n:
                if s[j] == "#":
                    break
                j +=  1
            
            results.append(s[j+1: 1+j+int(s[i:j])])
            i = 1+j+int(s[i:j])

        return results