class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def dfs(toopen: int, toclose: int, path: str) -> None:
            if not toopen and not toclose:
                results.append(path)
                return

            if toopen:
                dfs(toopen-1, toclose, path+"(")

            if path and toopen < toclose and toclose:
                dfs(toopen, toclose-1, path+")")



        dfs(n, n, "")
        return results