class WordDictionary:

    def __init__(self):
        self.words = {}

    def addWord(self, word: str) -> None:
        ref = self.words


        for char in word:
            ref[char] = {**ref.get(char, {})}
            ref = ref[char]

        ref["end"] = True

    def search(self, word: str) -> bool:
        # Start with the root trie in our list of tries to check
        refs = [self.words]

        for char in word:
            next_refs = []

            for ref in refs:
                if char == ".":
                    for key in ref.keys():
                        if key != "end":
                            next_refs.append(ref[key])
                else:
                    next_refs.append(ref.get(char, {}))
                
            refs = next_refs

        for ref in refs:
            if ref.get("end", False):
                return True
                
        return False
