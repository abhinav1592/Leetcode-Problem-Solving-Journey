from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        def get_sum(start, length):
            return prefix_sum[start + length] - prefix_sum[start]

        def solve_case(len1, len2):
            max_sum = 0
            # max_sum1_so_far is the maximum sum of a subarray of length len1
            # that ends at or before the start of the current subarray of length len2
            max_sum1_so_far = 0
            
            for i in range(len1, n - len2 + 1):
                # Sum of the current subarray of length len1
                current_sum1 = get_sum(i - len1, len1)
                max_sum1_so_far = max(max_sum1_so_far, current_sum1)
                
                # Sum of the current subarray of length len2
                current_sum2 = get_sum(i, len2)
                
                max_sum = max(max_sum, max_sum1_so_far + current_sum2)
            return max_sum

        # Case 1: L-length subarray first, then M-length subarray
        max1 = solve_case(firstLen, secondLen)
        
        # Case 2: M-length subarray first, then L-length subarray
        max2 = solve_case(secondLen, firstLen)
        
        return max(max1, max2)
        


Solution().maxSumTwoNoOverlap(nums=[1,2,3,4,5,6], firstLen=2, secondLen=3)