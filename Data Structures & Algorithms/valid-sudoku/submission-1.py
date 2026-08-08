class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        history = {i:{"col": set(), "row": set()} for i in range(n)}

        for x in range(n):
            for y in range(n):
                if not board[x][y].isdigit():
                    continue
                # visit col
                if board[x][y] in history[x]["col"]:
                    return False
                history[x]["col"].add(board[x][y]) 

                # visit row
                if board[x][y] in history[y]["row"]:
                    return False
                history[y]["row"].add(board[x][y])

                # visit box
                box = ((x // 3), (y // 3))
                history[box] = history.get(box, set())
                if board[x][y] in history[box]:
                    return False
                history[box].add(board[x][y])


        return True