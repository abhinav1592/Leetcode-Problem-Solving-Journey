from collections import defaultdict

class Solution:
    """
    Solution for the "Fruits into Baskets" problem.
    """
    def totalFruit(self, fruits: list[int]) -> int:
        """
        Calculates the maximum number of fruits that can be picked.

        This method uses a sliding window approach to find the longest
        subarray with at most two distinct elements.

        Args:
            fruits: A list of integers representing the types of fruits.

        Returns:
            The maximum number of fruits that can be picked.
        """
        if not fruits:
            return 0
        
        # Use a dictionary to keep track of the count of each fruit type in the current window.
        fruit_counts = defaultdict(int)
        
        left = 0
        max_length = 0
        
        # The 'right' pointer expands the window.
        for right in range(len(fruits)):
            # Add the current fruit to our window and update its count.
            fruit_counts[fruits[right]] += 1
            
            # The condition check: if we have more than two distinct fruit types,
            # we need to shrink the window from the left.
            while len(fruit_counts) > 2:
                # Get the fruit at the 'left' pointer.
                fruit_to_remove = fruits[left]
                
                # Decrement its count.
                fruit_counts[fruit_to_remove] -= 1
                
                # If the count becomes zero, it means this fruit type is no longer
                # in our window, so we can remove it from the dictionary.
                if fruit_counts[fruit_to_remove] == 0:
                    del fruit_counts[fruit_to_remove]
                
                # Shrink the window by moving the 'left' pointer.
                left += 1
            
            # After ensuring the window is valid (at most 2 distinct fruits),
            # calculate its length and update the maximum.
            current_length = right - left + 1
            max_length = max(max_length, current_length)
            
        return max_length