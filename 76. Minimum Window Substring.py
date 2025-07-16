'''
https://leetcode.com/problems/minimum-window-substring/description/
'''
class Solution:
    def check_if_t_in_included_in_s(self, freq_t, freq_s):
        for c in freq_t:
            if freq_t.get(c, 0) > freq_s.get(c, 0):
                return False
        return True
                
    def minWindow(self, s: str, t: str) -> str:
        freq_t = {}
        freq_s = {}
        debug = False
        for c in t:
            freq_t[c] = freq_t.get(c, 0) + 1
        if debug:
            print(f"freq_t: {freq_t}")
        start, end = 0, 0
        # intervals = []
        min_length_interval = float('inf')
        ans = ""
        while end < len(s):
            c = s[end]
            freq_s[c] = freq_s.get(c, 0) + 1
            # if debug:
            #     print(f"start: {start}, end: {end}, c:{c}, freq_s: {freq_s}")
            while end < len(s):
                if self.check_if_t_in_included_in_s(freq_t, freq_s):
                    interval_length = end - start + 1
                    if interval_length < min_length_interval:
                        ans = s[start: end + 1]
                        min_length_interval = interval_length
                    freq_s[s[start]] -= 1
                    start += 1
                else:
                    end += 1
                    break
        return ans


s = "a"
t = "aa"
print(Solution().minWindow(s=s, t=t))