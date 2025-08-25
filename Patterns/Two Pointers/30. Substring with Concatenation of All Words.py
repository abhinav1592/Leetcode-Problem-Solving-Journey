'''
Idea:
if len(s) - len(words) * len(words[0]) < 0:
    return []

0. Form two data structures-> 
     - freq_map of words having count
1. Loop through s from 0 till (len(s) - len(words) * len(words[0]))
   a. Fo
'''
from typing import List
from collections import defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        each_word_length = len(words[0])
        concatenated_word_length = len(words) * each_word_length
        if len(s) - concatenated_word_length < 0:
            return []
        
        freq_words = defaultdict(int)
        initial_letters = set()
        for word in words:
            freq_words[word] += 1
            initial_letters.add(word[0])
        
        print(f"freq_words: {freq_words}, initial_letters: {initial_letters}")
        ans = []
        for index in range(0, len(s) - concatenated_word_length + 1):
            if s[index] not in initial_letters:
                continue
            string_till_concatenated_word_length = s[index: index + concatenated_word_length]
            print(f"index: {index} string_till_concatenated_word_length: {string_till_concatenated_word_length}")
            string_freq_map = defaultdict(int)
            for string_index in range(0, len(string_till_concatenated_word_length), each_word_length):
                string_freq_map[string_till_concatenated_word_length[string_index: string_index + each_word_length]] += 1
            print(f"string_freq_map: {string_freq_map}")
            if string_freq_map == freq_words:
                ans.append(index)
                string_freq_map = None
        return ans


s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
print(Solution().findSubstring(s=s, words=words))

