'''
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Given a string s, find the length of the longest
substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
'''

class Solution1:
    def check_for_repeating_characters(self, p):
        r = False
        for x in p:
            if p[x] > 1:
                r = True
                break
        return r

    def lengthOfLongestSubstring(self, s: str) -> int:
        debug = False
        if s == "":
            return 0
        ans = float('-inf')
        start = 0
        p = {}
        for end in range(len(s)):
            p[s[end]] = p.get(s[end], 0) + 1
            if debug:
                print(f"psum: {p}")
            c = self.check_for_repeating_characters(p)
            if debug:
                print(f"[1] c: {c}, start: {start}, end: {end}, substring: {s[start: end+1]}")
            if c is False:
                ans = max(end - start + 1, ans)
            else:
                while (c):
                    if debug:
                        print(f"[while : 2] c: {c}, start: {start}, end: {end}, substring: {s[start: end+1]}")
                    p[s[start]] -= 1
                    start += 1
                    c = self.check_for_repeating_characters(p)
                ans = max(end - start + 1, ans)
            if debug:
                print(f"start: {start}, end: {end}, , substring: {s[start: end + 1]}, ans: {ans}")
                print("--" * 30)
        return ans


############## SOLUTION-2 ########################



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        # This dictionary stores the last index of each character.
        char_index_map = {}
        max_length = 0
        start = 0  # start pointer of the window
        longest_string_indexes = []
        for end in range(len(s)):
            current_char = s[end]

            # If the character is repeated, adjust the start pointer
            if current_char in char_index_map and char_index_map[current_char] >= start:
                start = char_index_map[current_char] + 1

            # Update the last seen index of the current character
            char_index_map[current_char] = end

            # Calculate the current window size and update max_length
            if end - start + 1 > max_length:
                longest_string_indexes = [start, end]
                max_length = end - start + 1

        print(f"longest string: {s[longest_string_indexes[0]: longest_string_indexes[1] + 1]}" )
        return max_length



s = 'abcddddabcdefssdfabcd'
print(Solution().lengthOfLongestSubstring(s))