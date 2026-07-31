class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        result = 0

        visited = set()
        n1 = len(text1)
        n2 = len(text2)
        q = [[0, 0, 0]]
        while q:
            p1, p2, counter = q.pop()

            if p1 >= n1 or p2 >= n2 or (p1, p2, counter) in visited:
                continue

            if text1[p1] == text2[p2]:
                q.append([p1+1, p2+1, counter+1])
                result = max(result, counter+1)
            else:
                q.extend([[p1+1, p2, counter], [p1, p2+1, counter]])

            visited.add((p1, p2, counter))

        return result