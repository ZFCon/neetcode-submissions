class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = dict()

        for word in strs:
            key = "".join(sorted(list(word)))
            results[key] = results.get(key, [])
            results[key].append(word)

        return [list(words) for words in results.values()]