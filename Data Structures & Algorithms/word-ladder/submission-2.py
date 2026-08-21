class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def generate_pattern(word: str) -> List[str]:
            for i in range(len(word)):
                yield word[:i] + "*" + word[i+1:]
        
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for pattern in generate_pattern(word):
                nei[pattern].append(word)
                
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                for pattern in generate_pattern(word):

                    for neiWord in nei[pattern]:

                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
                            
            res += 1
            
        return 0