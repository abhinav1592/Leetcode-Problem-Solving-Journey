class Solution:
    def longestPalindrome(self, s: str) -> int:
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left + 1: right]

        max_str = s[0]
        for center in range(len(s)):
            odd = expand_around_center(center, center)
            even = expand_around_center(center, center + 1)
            max_str = odd if len(odd) > len(max_str) else max_str
            max_str = even if len(even) > len(max_str) else max_str
        
        return max_str


# Sample usage
sol = Solution()
result = sol.longestPalindrome("babad")
print(f"\nResult: {result}")
