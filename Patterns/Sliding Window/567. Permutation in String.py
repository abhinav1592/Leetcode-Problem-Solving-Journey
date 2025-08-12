class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        string_1_freq, string_2_freq = [0] * 26, [0] * 26
        for index in range(len(s1)):
            string_1_freq[ord(s1[index]) - 97] += 1

        contains_permutation = False
        for end in range(len(s2)):
            string_2_freq[ord(s2[end]) - 97] += 1
            if end >= len(s1):
                string_2_freq[ord(s2[end - len(s1)]) - 97] -= 1
            if string_1_freq == string_2_freq:
                contains_permutation = True
        return contains_permutation