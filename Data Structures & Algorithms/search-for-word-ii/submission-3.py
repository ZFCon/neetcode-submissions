class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not words:
            return []

        trie = {}
        n = len(board)
        m = len(board[0])
        results = []

        # make a trie
        for word in words:
            ref = trie
            for char in word:
                ref[char] = ref.get(char, {})
                ref = ref[char]
            
            ref["end"] = word
        
        def dfs(x: int, y: int, ref: dict) -> str:
            if x < 0 or x >= n or y < 0 or y >= m or board[x][y] == 0 or ref.get(board[x][y]) is None:
                return

            char = board[x][y]
            ref = ref[char]
            board[x][y] = 0
            if "end" in ref:
                results.append(ref["end"])

            dfs(x+1, y, ref)
            dfs(x, y+1, ref)
            dfs(x-1, y, ref)
            dfs(x, y-1, ref)

            board[x][y] = char

        for x in range(n):
            for y in range(m):
                if board[x][y] != 0:
                    word = dfs(x, y, trie)

        return list(set(results))