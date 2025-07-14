'''
https://leetcode.com/problems/sliding-window-maximum/description/
'''
from typing import List
import heapq

class MaxHeap:
    def __init__(self):
        self._heap = []

    def push(self, item):
        # Push the negative of the item to simulate a max heap
        heapq.heappush(self._heap, -item)

    def pop(self):
        if not self._heap:
            raise IndexError("pop from empty max heap")
        # Pop the smallest negative value and negate it to get the largest positive
        return -heapq.heappop(self._heap)

    def peek(self):
        if not self._heap:
            raise IndexError("peek from empty max heap")
        return -self._heap[0]

    def is_empty(self):
        return len(self._heap) == 0

class Solution_attempted_using_heap:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = MaxHeap()
        ans = []
        if k == 1:
            return nums
        for index in range(len(nums)):
            if index >= k - 1:
                ans.append(max_heap.peek())
                if max_heap.peek() == nums[index - 1]:
                    max_heap.pop()
                max_heap.push(nums[index])
            else:
                max_heap.push(nums[index])
        return ans


nums = [1,3,-1,-3,5,3,6,7]
k = 3

# nums = [7, 2, 4]
# k = 2


'''
You are trying to use a max heap, but the problem is that in a heap, there is no direct way to remove a specific element efficiently (other than the root).

In the sliding window problem, each time you slide forward, you need to:
1️⃣ Insert the new element.
2️⃣ Remove the element that just went out of the window.

In your code, you are only popping when max_heap.peek() == nums[index - 1], which is not correct. You need to remove the exact element that exited the window, not just the max.

'''


from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int, debug: bool = False) -> List[int]:
        """
        Find maximum in each sliding window of size k.
        :param nums: List of integers
        :param k: Window size
        :param debug: If True, print internal debug statements
        :return: List of maximums for each window
        """
        q = deque()  # Store indices, not actual values
        res = []

        for i in range(len(nums)):
            # Remove indices out of current window (leftmost index <= i - k)
            if q and q[0] <= i - k:
                if debug:
                    print(f"Index {q[0]} (value {nums[q[0]]}) is out of window. Removing from deque.")
                q.popleft()

            # Remove indices whose corresponding values are smaller than nums[i]
            while q and nums[i] >= nums[q[-1]]:
                if debug:
                    print(f"Value at index {q[-1]} ({nums[q[-1]]}) is smaller than or equal to current value {nums[i]}. Removing from deque.")
                q.pop()

            # Add current index to deque
            q.append(i)
            if debug:
                print(f"Added index {i} (value {nums[i]}). Current deque: {[nums[idx] for idx in q]}")

            # Append result when we have a full window
            if i >= k - 1:
                if debug:
                    print(f"Window [{i - k + 1}, {i}]: max value is {nums[q[0]]}")
                res.append(nums[q[0]])
            print("----" * 40)

        return res

# Example usage with debug flag
if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    sol = Solution()
    result = sol.maxSlidingWindow(nums, k, debug=True)
    print("Final Result:", result)




print(Solution().maxSlidingWindow(nums=nums,k=k))