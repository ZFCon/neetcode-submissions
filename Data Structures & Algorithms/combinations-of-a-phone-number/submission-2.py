class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        results = []

        def dfs(index: int, path: str) -> None:
            if len(path) == len(digits):
                results.append(path)
                return

            for char in phone_map[digits[index]]:
                dfs(index+1, path+char)

            
        dfs(0, "")
        return results