'''
Link: https://leetcode.com/problems/k-radius-subarray-averages/description/
'''
from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        prefix_sums = [0] * len(nums)
        prefix_sums[0] = nums[0]
        for index in range(1, len(nums)):
            prefix_sums[index] = nums[index] + prefix_sums[index - 1]
        print(f" prefix_sums: {prefix_sums}")
        divisor = 2 * k + 1
        averages = []
        for index in range(len(nums)):
            average = None
            if index < k:
                average = -1
            else:
                start_index = index - k
                end_index = index + k
                print(f"start_index: {start_index}, end_index: {end_index}, len(nums): {len(nums)}")
                # check whether the end is within the bounds
                if end_index < len(nums):
                    if start_index == 0:
                        average = prefix_sums[end_index] // divisor
                    else:
                        print(f"prefix_sums[{end_index}] - prefix_sums[{start_index}] : {prefix_sums[end_index] - prefix_sums[start_index - 1]}")
                        average = (prefix_sums[end_index] - prefix_sums[start_index]) // divisor
                else:
                    average = -1
            if average is not None:
                averages.append(average)
            else:
                print(f"For index: {index}, prefix_sums: {prefix_sums}, average is None.")
        return averages


nums = [40527,53696,10730,66491,62141,83909,78635,18560]
k = 2

print(Solution().getAverages(nums=nums, k=k))
