'''
https://leetcode.com/problems/4sum/description/


'''
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        if len(nums) < 4:
            return results
        
        n = sorted(nums)
        for i in range(n-4):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-3):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                right = n - 1
                left = j + 1
                two_sum_target = target - nums[i] - nums[j]
                while left < right:
                    current_sum = nums[left] + nums[right]
                    if current_sum == two_sum_target:
                        results.append(nums[i], nums[j], nums[left], nums[right])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    else:
                        if current_sum < two_sum_target:
                            left += 1
                        else:
                            right -= 1
        return results