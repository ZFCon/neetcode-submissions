class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        UP = [-1, 0]
        DOWN = [1, 0]
        LEFT = [0, -1]
        RIGHT = [0, 1]
        visited = set()

        def dfs(x: int, y: int, i: int) -> bool:
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[i] or (x, y) in visited:
                return False
            if i == len(word) - 1:
                return True

            visited.add((x, y))
            # Check all directions: if any one returns True, the result is True
            result = (dfs(x + UP[0], y + UP[1], i + 1) or 
                    dfs(x + DOWN[0], y + DOWN[1], i + 1) or 
                    dfs(x + LEFT[0], y + LEFT[1], i + 1) or 
                    dfs(x + RIGHT[0], y + RIGHT[1], i + 1))
            visited.remove((x, y))

            return result
            
        

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
        