class PrefixTree:

    def __init__(self):
        self.word = {}

    def insert(self, word: str) -> None:
        ref = self.word
        for char in word:
            ref[char] = {**ref.get(char, {})}
            ref = ref[char]
        ref["end"] = True

    def search(self, word: str) -> bool:
        ref = self.word
        for char in word:
            ref = ref.get(char, {})

        return ref.get("end", False)

    def startsWith(self, prefix: str) -> bool:
        ref = self.word
        for char in prefix:
            ref = ref.get(char, None)

            if ref is None:
                return False
        return True
        