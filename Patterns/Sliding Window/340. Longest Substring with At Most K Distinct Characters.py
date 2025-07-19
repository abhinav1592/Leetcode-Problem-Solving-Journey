'''
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
'''

from collections import Counter

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        start = 0
        end = 0
        ans = 0
        freq = Counter()
        while end < len(s):
            freq[s[end]] += 1

            # Contract the window if the frequency is exceeding
            while len(freq) > k:
                freq[s[start]] -= 1
                if freq[s[start]] == 0:
                    del freq[s[start]]
                start += 1
            ans = max(ans, end - start + 1)
            end += 1
        return ans



s = "eceba"
k = 2
print(Solution().lengthOfLongestSubstringKDistinct(s=s, k=k))





from collections import defaultdict
import time
import random

# --- Simulate an infinite stream ---
def infinite_char_stream(source_string: str):
    """A generator that yields characters from a source string indefinitely.
       In a real scenario, this would read from an external source.
    """
    idx = 0
    while True:
        if not source_string: # Handle empty source string
            time.sleep(0.1) # Simulate waiting for data
            continue
        yield source_string[idx % len(source_string)]
        idx += 1
        # time.sleep(0.01) # Simulate delay in stream data arrival

# --- The solution for infinite stream ---
def lengthOfLongestSubstringKDistinct_stream(stream_source, k: int) -> int:
    if k == 0:
        return 0
    
    char_counts = defaultdict(int)
    left = 0              # Absolute position of the left pointer in the stream
    max_length = 0
    current_right_pos = 0 # Absolute position of the character currently being processed

    try:
        # Iterate through the stream, character by character
        for current_char in stream_source:
            # 1. Expand the window (right pointer implicitly moves with current_right_pos)
            char_counts[current_char] += 1
            
            # 2. Shrink the window if distinct characters exceed k
            while len(char_counts) > k:
                # The character at the 'left' boundary of our current window
                # We don't have the full string, so we rely on 'left' and the counts.
                # This is the key difference: we don't 'look up' s[left],
                # we just logically advance 'left' and decrement its count.
                
                # To get the character at 'left', we'd need to store the window's actual characters
                # in a deque. However, if we only need the *length*, we don't need the characters
                # themselves, only their counts and the 'left' pointer.
                # The challenge is knowing *which* character is at 'left' to decrement its count.
                #
                # This is where the standard O(N) HashMap approach shines.
                # The 'left' pointer advances, and we decrement the count of the character
                # that *was* at the old 'left' position.
                #
                # For a true stream, if you don't store the window's characters, you can't
                # know s[left]. This implies that the standard O(N) solution *already* works
                # for streams because it only ever needs s[right] and the character that *was*
                # at s[left] when left advances.
                #
                # Let's re-evaluate: The original O(N) solution relies on `s[left]` to know
                # which character to remove. For an infinite stream, you *must* store the
                # characters within the current window if you need to know `s[left]`.

                # --- Corrected logic for stream (requires storing window characters) ---
                # To know s[left], we need a buffer that holds the current window's characters.
                # collections.deque is ideal for this.
                
                # This makes the solution O(N) for time (amortized deque ops) and O(W) for space,
                # where W is the max window size. If W can be very large, this is still a memory concern.
                # But for this problem, W <= N, and for a stream, W <= current_right_pos.
                # The maximum possible window length is N (or current_right_pos if infinite).
                #
                # If k is small, the max window size is bounded. If k is large, the window can be huge.

                # Let's assume the problem implies a practical scenario where the window can fit in memory.
                # If the window itself can exceed memory, then it becomes a much harder problem
                # requiring external memory algorithms or distributed processing, as discussed before.
                
                # For this problem, the standard sliding window with `char_counts` and a `deque`
                # to store the actual characters in the window is the most direct adaptation.
                
                # --- Let's restart the conceptual code with a deque ---
                pass # This part will be in the actual code block below
            
            # Update max_length for the current valid window
            # The length is (current_right_pos - left + 1)
            # current_right_pos here is the 0-indexed position of the *current_char*
            max_length = max(max_length, current_right_pos - left + 1)
            
            current_right_pos += 1 # Advance global right pointer for the next iteration

    except StopIteration: # Stream ended (for simulated streams)
        print("Stream ended.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return max_length

# --- Actual implementation with deque for stream ---
from collections import defaultdict, deque

def lengthOfLongestSubstringKDistinct_stream_actual(stream_source, k: int) -> int:
    if k == 0:
        return 0
    
    char_counts = defaultdict(int)
    window_chars = deque() # Stores characters currently in the window
    left_abs_pos = 0     # Absolute starting position in the stream
    max_length = 0

    try:
        # Iterate through the stream, character by character
        # current_abs_pos represents the absolute index of the character being read
        for current_abs_pos, current_char in enumerate(stream_source):
            # 1. Expand the window (add current_char to the right)
            window_chars.append(current_char)
            char_counts[current_char] += 1
            
            # 2. Shrink the window if distinct characters exceed k
            while len(char_counts) > k:
                left_char = window_chars.popleft() # Remove from the left of the window
                char_counts[left_char] -= 1
                if char_counts[left_char] == 0:
                    del char_counts[left_char]
                left_abs_pos += 1 # Advance the absolute left pointer
            
            # 3. Update max_length for the current valid window
            # Current window length is (current_abs_pos - left_abs_pos + 1)
            max_length = max(max_length, current_abs_pos - left_abs_pos + 1)
            
    except StopIteration: # This is how a generator signals exhaustion
        print("Stream ended.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return max_length

# --- Test Cases for Stream ---

# Simulate a finite stream for testing
def finite_stream_generator(s: str):
    for char in s:
        yield char

print("--- Stream Tests ---")
print(f"Stream 'eceba', k=2 -> {lengthOfLongestSubstringKDistinct_stream_actual(finite_stream_generator('eceba'), 2)}") # Expected: 3
print(f"Stream 'aa', k=1 -> {lengthOfLongestSubstringKDistinct_stream_actual(finite_stream_generator('aa'), 1)}")    # Expected: 2
print(f"Stream 'abaccc', k=2 -> {lengthOfLongestSubstringKDistinct_stream_actual(finite_stream_generator('abaccc'), 2)}") # Expected: 4
print(f"Stream '', k=0 -> {lengthOfLongestSubstringKDistinct_stream_actual(finite_stream_generator(''), 0)}")      # Expected: 0
print(f"Stream 'a', k=0 -> {lengthOfLongestSubstringKDistinct_stream_actual(finite_stream_generator('a'), 0)}")     # Expected: 0
print(f"Stream 'a', k=1 -> {lengthOfLongestSubstringKDistinct_stream_actual(finite_stream_generator('a'), 1)}")     # Expected: 1

# Simulate a longer stream
long_string = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" * 10000 # 520,000 chars
print(f"Stream (long), k=3 -> {lengthOfLongestSubstringKDistinct_stream_actual(finite_stream_generator(long_string), 3)}")
# Expected: 3 (e.g., 'abc', 'bcd', etc.)

# Simulate a stream where k is large
print(f"Stream 'abcde', k=5 -> {lengthOfLongestSubstringKDistinct_stream_actual(finite_stream_generator('abcde'), 5)}") # Expected: 5
print(f"Stream 'abcde', k=10 -> {lengthOfLongestSubstringKDistinct_stream_actual(finite_stream_generator('abcde'), 10)}") # Expected: 5
