'''
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
'''

from collections import Counter

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        start = 0
        end = 0
        ans = 0
        freq = Counter()
        while end < len(s):
            freq[s[end]] += 1

            # Contract the window if the frequency is exceeding
            while len(freq) > k:
                freq[s[start]] -= 1
                if freq[s[start]] == 0:
                    del freq[s[start]]
                start += 1
            ans = max(ans, end - start + 1)
            end += 1
        return ans



s = "eceba"
k = 2
print(Solution().lengthOfLongestSubstringKDistinct(s=s, k=k))