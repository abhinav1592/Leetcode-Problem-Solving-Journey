'''
Longest subarray having only k zeros -> with k = 1 here
'''
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if nums.count(0) == 0:
            return len(nums) - 1
        start = 0
        nums_of_zeros = 0
        max_window = 0
        k = 1
        for end in range(len(nums)):
            if nums[end] == 0:
                nums_of_zeros += 1

            while (nums_of_zeros > k):
                if nums[start] == 0:
                    nums_of_zeros -= 1
                start += 1

            current_window = end - start + 1
            max_window = max(max_window, current_window)
        return max_window - 1