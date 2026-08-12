class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        result = ""

        for i in range(n):
            result += word1[i]
            result += word2[i]

        result += word1[n:]
        result += word2[n:]
        
        return result