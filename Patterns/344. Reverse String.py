from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) % 2 == 0:
            left, right = len(s) // 2 - 1, len(s) // 2
        else:
            left, right = len(s) // 2 - 1, len(s) // 2 + 1
        while left != -1 and right != len(s):
            left_character = s[left]
            right_character = s[right]
            s[left] = right_character
            s[right] = left_character
            left -= 1
            right += 1