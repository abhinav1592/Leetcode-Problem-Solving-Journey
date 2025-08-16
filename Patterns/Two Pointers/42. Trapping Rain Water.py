'''
DP Approach:

Algorithm:

1. Handle edge cases: if n < 3, no water can be trapped. Return 0.

2. Create two arrays left_max and right_max of the same size as height.

3. Populate left_max:
a. left_max[0] = height[0].
b. Iterate from i = 1 to n-1: left_max[i] = max(left_max[i-1], height[i]). This stores the maximum height encountered so far from the left.

4. Populate right_max:
a. right_max[n-1] = height[n-1].
b. Iterate from i = n-2 down to 0: right_max[i] = max(right_max[i+1], height[i]). This stores the maximum height from the right.

5. Initialize total_water = 0.

6. Iterate through the height array from i = 0 to n-1.

7. For each index i:
a. Calculate the water trapped: min(left_max[i], right_max[i]) - height[i].
b. Add this amount to total_water.

8. Return total_water.

'''
from typing import List


class Solution_DP:
    def trap(self, height: List[int]) -> int:
        # DP approach
        n = len(height)
        # 1
        if n < 3: return 0
        # 2
        left_max, right_max = [0] * n, [0] * n
        # 3 -  This stores the maximum height encountered so far from the left
        left_max[0] = height[0]
        for index in range(1, n):
            left_max[index] = max(left_max[index-1], height[index])
        # 4 - This stores the maximum height from the right.
        right_max[-1] = height[-1]
        for index in range(n-2, -1, -1):
            right_max[index] = max(right_max[index+1], height[index])
        # 5
        total_water = 0
        # 6 and 7
        for index in range(n):
            total_water += min(left_max[index], right_max[index]) - height[index]
        # 8
        return total_water




'''
Two Pointer Approach:

Algorithm:

1. Initialize l = 0, r = n-1, total_water = 0, left_max = 0, right_max = 0.

2. While l < r:
    a. If height[l] <= height[r]:
        i. If height[l] >= left_max: left_max = height[l] (update the max).
        ii. Else: total_water += left_max - height[l] (trap water).
        iii. l++.
    b. Else (height[l] > height[r]):
        i. If height[r] >= right_max: right_max = height[r] (update the max).
        ii. Else: total_water += right_max - height[r] (trap water).
        iii. r--.

3. Return total_water.
'''
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # Two pointer approach
        n = len(height)
        if n < 3: return 0
        # 1
        left = 0
        right = n - 1
        total_water = 0
        left_max = 0
        right_max = 0
        # 2
        while left < right:
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = max(left_max, height[left])
                else:
                    total_water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = max(right_max, height[right])
                else:
                    total_water += right_max - height[right]
                right -= 1
        # 3
        return total_water