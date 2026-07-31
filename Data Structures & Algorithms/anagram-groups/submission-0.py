class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}

        for text in strs:
            key = "".join(sorted(text))

            if key not in results:
                results[key] = []
            results[key].append(text)

        return list(results.values())