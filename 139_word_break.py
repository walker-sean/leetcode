# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set(wordDict)
        
        if not len(s):
            return True
        
        word_endings = []
        
        for i in range(len(s)):
            if (s[0:i + 1] in word_dict):
                word_endings.append(i)
                continue
            for ending in word_endings:
                if s[ending + 1:i + 1] in word_dict:
                    word_endings.append(i)
                    break
        
        return word_endings.pop() == len(s) - 1