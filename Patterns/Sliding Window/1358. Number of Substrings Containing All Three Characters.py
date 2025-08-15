from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        freq_s = defaultdict(int)
        number_of_substrings = 0
        n = len(s)

        for right in range(n):
            freq_s[s[right]] += 1

            # Shrink while window has at least one of each 'a','b','c'
            while freq_s['a'] > 0 and freq_s['b'] > 0 and freq_s['c'] > 0:
                # Every extension to the right is valid
                number_of_substrings += n - right
                freq_s[s[left]] -= 1
                left += 1

        return number_of_substrings
