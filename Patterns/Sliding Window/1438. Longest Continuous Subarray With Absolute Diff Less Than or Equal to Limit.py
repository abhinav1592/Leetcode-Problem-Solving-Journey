from typing import List
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        min_deque, max_deque = deque(), deque()
        maxLength = 0
        for right in range(len(nums)):
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                if min_deque[0] == left:
                    min_deque.popleft()
                if max_deque[0] == left:
                    max_deque.popleft()
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength


nums = [10,1,2,4,7,2]
limit = 5
print(Solution().longestSubarray(nums=nums, limit=limit))