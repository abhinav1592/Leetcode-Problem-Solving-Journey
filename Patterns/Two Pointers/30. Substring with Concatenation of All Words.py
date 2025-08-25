'''
Idea:
if len(s) - len(words) * len(words[0]) < 0:
    return []

0. Form two data structures-> 
     - freq_map of words having count
1. Loop through s from 0 till (len(s) - len(words) * len(words[0]))
   a. Keep adding words to a temporary word counter
   b. Match them
'''
from typing import List
from collections import defaultdict


class Solution_by_brute_force:
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

# From Gemini
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_counts = Counter(words)
        result = []

        # We need to run L independent sliding windows.
        for i in range(word_len):
            left = i
            current_counts = Counter()
            words_found = 0

            # The right pointer slides one word at a time.
            for j in range(i, len(s) - word_len + 1, word_len):
                current_word = s[j : j + word_len]

                if current_word in word_counts:
                    current_counts[current_word] += 1
                    words_found += 1

                    # Check for over-frequency and shrink window if needed.
                    while current_counts[current_word] > word_counts[current_word]:
                        left_word = s[left : left + word_len]
                        current_counts[left_word] -= 1
                        words_found -= 1
                        left += word_len

                    # Check for a valid concatenation.
                    if words_found == num_words:
                        result.append(left)

                        # Found a solution, now move the window one word to the right.
                        # This is crucial for handling overlapping solutions.
                        found_word = s[left : left + word_len]
                        current_counts[found_word] -= 1
                        words_found -= 1
                        left += word_len

                else:
                    # Invalid word found. Reset the window.
                    current_counts.clear()
                    words_found = 0
                    left = j + word_len

        return result

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
print(Solution().findSubstring(s=s, words=words))

