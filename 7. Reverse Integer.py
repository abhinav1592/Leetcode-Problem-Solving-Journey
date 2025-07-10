'''
Link: https://leetcode.com/problems/reverse-integer/description/

7. Reverse Integer
Solved
Medium
Topics
conpanies icon
Companies
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 
'''


class Solution:
    def remove_leading_zeros(self, string_number):
        num = []
        index = 0
        while index < len(string_number):
            if string_number[index] == 0:
                index += 1
            else:
                break
        return string_number[index:]
        
    def reverse(self, x: int) -> int:
        range_min = (-1) * 2**31
        range_max = 2**31 - 1
        if x > range_max or x < range_min:
            return 0
        else:
            string_format = str(x)
            if len(string_format) > 0:
                minus_sign = False
                if string_format[0] == "-":
                    reversed_number = string_format[1:][::-1]
                    minus_sign = True
                else:
                    reversed_number = string_format[::-1]
                reversed_number = self.remove_leading_zeros(
                    reversed_number)
                if minus_sign:
                    reversed_number = "-" + reversed_number
            if int(reversed_number) > range_max or int(reversed_number) < range_min:
                return 0
            else:
                return int(reversed_number)


class Solution_official:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        rev, x = 0, abs(x)
        while x:
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod
            if rev > 2**31 - 1:
                return 0
        return sign * rev