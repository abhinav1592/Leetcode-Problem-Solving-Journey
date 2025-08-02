class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start, end, num_zeros, max_length = 0, 0, 0, 0
        while end < len(nums):
            if nums[end] == 0:
                num_zeros += 1
            while num_zeros > k:
                if nums[start] == 0:
                    num_zeros -= 1
                start += 1
            
            max_length = max(max_length, end - start + 1)
            end += 1
        return max_length