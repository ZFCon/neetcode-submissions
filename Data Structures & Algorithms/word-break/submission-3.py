class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        q = [[0, 1]]

        max_word_length = len(max(wordDict, key=len))
        visited = set()

        while q:
            i, j = q.pop()
            
            if j > n or (j-i) > max_word_length or (i, j) in visited:
                continue

            visited.add((i, j))

            if s[i:j] in wordDict:
                if j == n:
                    return True
                q.extend([[i, j], [j, j+1]])
                
            q.append([i, j+1])

        return False