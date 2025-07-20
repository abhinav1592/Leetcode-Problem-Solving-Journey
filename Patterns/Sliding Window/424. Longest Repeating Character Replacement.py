'''
https://leetcode.com/problems/longest-repeating-character-replacement/description/
'''
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        max_len = 0
        max_freq = 0  # Stores the maximum frequency of any character in the current window
        char_counts = defaultdict(int)

        for right in range(n):
            char_counts[s[right]] += 1
            max_freq = max(max_freq, char_counts[s[right]])

            # Check if the current window is invalid
            # An invalid window means: (current_window_length - max_freq) > k
            # i.e., the number of characters to change is greater than k
            if (right - left + 1) - max_freq > k:
                # If invalid, shrink the window from the left
                char_counts[s[left]] -= 1
                left += 1
            
            # The window (right - left + 1) is always a potential candidate for max_len
            # because we only shrink it when it becomes invalid.
            # When it's valid, we take its length. When it shrinks, it's to find a new valid window.
            # max_len will capture the largest valid window encountered.
            max_len = max(max_len, right - left + 1)

        return max_len