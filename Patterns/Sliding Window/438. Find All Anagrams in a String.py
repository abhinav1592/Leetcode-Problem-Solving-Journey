'''
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
'''
from typing import List
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        ctr_s = defaultdict(int)
        ctr_p = defaultdict(int)
        for index in range(len(p)):
            ctr_p[p[index]] += 1
            ctr_s[s[index]] += 1
        
        indexes = []
        if ctr_p == ctr_s:
            indexes.append(0)

        for index in range(len(p), len(s)):
            print(f"s[{index} - {len(p)}]: {s[index - len(p)]}")
            ctr_s[s[index - len(p)]] -= 1
            ctr_s[s[index]] += 1
            if ctr_s == ctr_p:
                indexes.append(index - len(p) + 1)
        return indexes


s = "cbaebabacd"
p = "abc"
print(Solution().findAnagrams(s=s, p=p))