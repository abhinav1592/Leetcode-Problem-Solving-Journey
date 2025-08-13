from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        front_sum = [0] * (k + 1)
        back_sum = [0] * (k + 1)

        for i in range(1, k + 1):
            front_sum[i] = front_sum[i - 1] + cardPoints[i - 1]      # Take from front
            back_sum[i] = back_sum[i - 1] + cardPoints[n - i]        # Take from back

        max_points = 0
        for i in range(k + 1):
            max_points = max(max_points, front_sum[i] + back_sum[k - i])

        return max_points
