class Solution:
    def isValid(self, text: str) -> bool:
       return list(text) == list(reversed(text) )

    def partition(self, s: str) -> List[List[str]]:
        results = []

        def dfs(start: int, path: List[str]) -> None:
            if start == len(s):
                results.append(path)
                return

            for i in range(start, len(s)):
                current_text = s[start:i+1]

                if self.isValid(current_text):
                    dfs(i+1, path + [current_text])


        dfs(0, [])
        return results