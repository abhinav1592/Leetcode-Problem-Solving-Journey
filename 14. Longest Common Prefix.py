class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def lcp_pair(s1, s2):
            ans = ""
            for index in range(min(len(s1), len(s2))):
                if s1[index] == s2[index]:
                    ans += s1[index]
                else:
                    break
            return ans
        
        if len(strs) <= 1:
            return strs[0]
        ans = None
        for index in range(len(strs) - 1):
            if ans is None:
                ans = lcp_pair(strs[index], strs[index + 1])
                if ans == "":
                    return ans
            else:
                ans = lcp_pair(ans, strs[index + 1])
        return ans
