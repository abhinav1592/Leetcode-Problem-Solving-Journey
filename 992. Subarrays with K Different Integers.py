'''
https://leetcode.com/problems/subarrays-with-k-different-integers/description/

This solution is wrong -> will correct it during revision

'''
from typing import List

class Solution_original:
    def check_if_frequency_dictionary_is_having_k_keys(self, d, k):
        return len(d.keys()) == k
    
    def decrement_element_count_and_delete_if_required(self, d, element):
        if d.get(element) > 0:
            d[element] -= 1
            if d.get(element) == 0:
                del d[element]
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        start, end = 0, 0
        num_of_subarrays = 0
        frequency_of_elements = {}
        while end < len(nums):
            frequency_of_elements[nums[end]] = frequency_of_elements.get(nums[end], 0) + 1
            if self.check_if_frequency_dictionary_is_having_k_keys(frequency_of_elements, k):
                num_of_subarrays += 1
                end += 1
            else:
                self.decrement_element_count_and_delete_if_required(frequency_of_elements, nums[end])
                while self.check_if_frequency_dictionary_is_having_k_keys(frequency_of_elements, k):
                    self.decrement_element_count_and_delete_if_required(frequency_of_elements, nums[start])
                    num_of_subarrays += 1
                    start += 1
        return num_of_subarrays



from typing import List

class Solution:
    def check_if_frequency_dictionary_is_having_k_keys(self, d, k, debug_flag=False):
        if debug_flag: print(f"DEBUG: Entering check_if_frequency_dictionary_is_having_k_keys with d={d}, k={k}")
        if debug_flag: print(f"DEBUG: len(d.keys()) = {len(d.keys())}, k={k}")
        result = len(d.keys()) == k
        if debug_flag: print(f"DEBUG: Returning {result} from check_if_frequency_dictionary_is_having_k_keys")
        return result
    
    def decrement_element_count_and_delete_if_required(self, d, element, debug_flag=False):
        if debug_flag: print(f"DEBUG: Entering decrement_element_count_and_delete_if_required with d={d}, element={element}")
        if debug_flag: print(f"DEBUG: Checking if d.get({element}) > 0")
        if d.get(element) > 0:
            if debug_flag: print(f"DEBUG: d[{element}] before decrement: {d[element]}")
            d[element] -= 1
            if debug_flag: print(f"DEBUG: d[{element}] after decrement: {d[element]}")
            if debug_flag: print(f"DEBUG: Checking if d.get({element}) == 0")
            if d.get(element) == 0: # Note: This should be d[element] == 0, not d.get(element)
                if debug_flag: print(f"DEBUG: Deleting element {element} from dictionary")
                del d[element]
        if debug_flag: print(f"DEBUG: Exiting decrement_element_count_and_delete_if_required, d={d}")
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        debug_flag=True
        if debug_flag: print(f"DEBUG: Entering subarraysWithKDistinct with nums={nums}, k={k}")
        start, end = 0, 0
        if debug_flag: print(f"DEBUG: Initializing start={start}, end={end}")
        num_of_subarrays = 0
        if debug_flag: print(f"DEBUG: Initializing num_of_subarrays={num_of_subarrays}")
        frequency_of_elements = {}
        if debug_flag: print(f"DEBUG: Initializing frequency_of_elements={frequency_of_elements}")
        while end < len(nums):
            if debug_flag: print(f"DEBUG: Start of while loop, end={end}, nums[end]={nums[end]}")
            frequency_of_elements[nums[end]] = frequency_of_elements.get(nums[end], 0) + 1
            if debug_flag: print(f"DEBUG: frequency_of_elements updated: {frequency_of_elements}")
            while not self.check_if_frequency_dictionary_is_having_k_keys(frequency_of_elements, k, debug_flag):
                end += 1
            num_of_subarrays += 1

                if debug_flag: print("--" * 5 + "IF CONDITION" + "--" * 5)
                if debug_flag: print(f"DEBUG: Condition met: check_if_frequency_dictionary_is_having_k_keys returned True")
                num_of_subarrays += 1
                if debug_flag: print(f"DEBUG: num_of_subarrays incremented to {num_of_subarrays}")
                end += 1
                if debug_flag: print(f"DEBUG: end incremented to {end}")
            else:
                if debug_flag: print("--" * 5 + "ELSE CONDITION" + "--" * 5)
                if debug_flag: print(f"DEBUG: Condition not met: check_if_frequency_dictionary_is_having_k_keys returned False")
                self.decrement_element_count_and_delete_if_required(frequency_of_elements, nums[end], debug_flag)
                if debug_flag: print(f"DEBUG: After decrementing nums[end], frequency_of_elements={frequency_of_elements}")
                while self.check_if_frequency_dictionary_is_having_k_keys(frequency_of_elements, k, debug_flag):
                    if debug_flag: print(f"DEBUG: Inner while loop, check_if_frequency_dictionary_is_having_k_keys returned True")
                    self.decrement_element_count_and_delete_if_required(frequency_of_elements, nums[start], debug_flag)
                    if debug_flag: print(f"DEBUG: After decrementing nums[start], frequency_of_elements={frequency_of_elements}")
                    num_of_subarrays += 1
                    if debug_flag: print(f"DEBUG: num_of_subarrays incremented to {num_of_subarrays}")
                    start += 1
                    if debug_flag: print(f"DEBUG: start incremented to {start}")
                end += 1 # This line seems out of place in your original logic, likely an error.
                if debug_flag: print(f"DEBUG: end incremented to {end} in else block")
            if debug_flag: print("**" * 10)

        if debug_flag: print(f"DEBUG: Exiting while loop. Final num_of_subarrays={num_of_subarrays}")
        return num_of_subarrays



nums = [1,2,1,2,3]
k = 2
print(Solution().subarraysWithKDistinct(nums=nums, k=k))