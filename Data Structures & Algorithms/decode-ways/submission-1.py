class Solution:
    def numDecodings(self, s: str) -> int:
        chars = {
            "1": "A",
            "2": "B",
            "3": "C",
            "4": "D",
            "5": "E",
            "6": "F",
            "7": "G",
            "8": "H",
            "9": "I",
            "10": "J",
            "11": "K",
            "12": "L",
            "13": "M",
            "14": "N",
            "15": "O",
            "16": "P",
            "17": "Q",
            "18": "R",
            "19": "S",
            "20": "T",
            "21": "U",
            "22": "V",
            "23": "W",
            "24": "X",
            "25": "Y",
            "26": "Z"
        }
        counter = [0]
        memo = {}

        def dfs(text: str) -> int:
            if text == "":
                return 1
            
            if text in memo:
                return memo[text]

            ways = 0

            for limit in range(2, 0, -1):
                if len(text) >= limit and text[:limit] in chars:
                    ways += dfs(text[limit:])

            memo[text] = ways

            return ways

        return dfs(s)

