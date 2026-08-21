from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
            
        wordList.append(beginWord)
        
        def is_similar(word1: str, word2: str) -> bool:
            diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1
                if diff > 1:
                    return False
            return diff == 1

        def list_of_words_similar(index: int) -> List[int]:
            similar_indices = []
            target_word = wordList[index]
            
            for i in range(len(wordList)):
                # Skip comparing the word to itself
                if i != index and is_similar(target_word, wordList[i]):
                    similar_indices.append(i)
                    
            return similar_indices
            
        # Helper to calculate how many characters differ from the target
        def diff_from_target(index: int) -> int:
            word = wordList[index]
            diff = 0
            for i in range(len(word)):
                if word[i] != endWord[i]:
                    diff += 1
            return diff

        n = len(wordList)
        
        # Track visited indices to prevent infinite loops
        visited = set([n - 1])
        
        q = deque([[n - 1, list_of_words_similar(n - 1), 1]])

        while q:
            i, words_index, c = q.popleft()

            if wordList[i] == endWord:
                return c

            # Sort the indices so words closest to endWord come first
            words_index.sort(key=diff_from_target)

            for j in words_index:
                if j not in visited:
                    visited.add(j)
                    q.append([j, list_of_words_similar(j), c + 1])

        return 0