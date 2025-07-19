'''
https://leetcode.com/problems/minimum-window-subsequence/description/
'''
class Solution:
    def minWindow(self, s1, s2):
        debug=True
        S = s1
        T = s2

        if debug:
            print(f"Input S: {S}")
            print(f"Input T: {T}")

        # Find - Get ending point of subsequence starting after S[s]
        def find_subseq(s):
            if debug:
                print(f"\nCalling find_subseq from index: {s}")
            t = 0
            # original_s = s
            while s < len(S):
                if debug:
                    print(f"  Comparing S[{s}] = {S[s]} with T[{t}] = {T[t]}")
                if S[s] == T[t]:
                    t += 1
                    if debug:
                        print(f"    Match found, advancing T to {t}")
                    if t == len(T):
                        break
                s += 1
            if debug:
                if t == len(T):
                    print(f"  Subsequence matched ending at index: {s}")
                else:
                    print("  Subsequence not found")
            print('*' * 10)
            return s if t == len(T) else None

        # Improve - Get best starting point of subsequence ending at S[s]
        def improve_subseq(s):
            if debug:
                print(f"Calling improve_subseq from index: {s}")
            t = len(T) - 1
            while t >= 0:
                if debug:
                    print(f"  Comparing S[{s}] = {S[s]} with T[{t}] = {T[t]}")
                if S[s] == T[t]:
                    t -= 1
                    if debug:
                        print(f"    Match found, moving T to {t}")
                s -= 1
            if debug:
                print(f"  Improved start index: {s + 1}")
            print('=' * 10)
            return s + 1

        s, min_len, min_window = 0, float('inf'), ''

        while s < len(S):
            end = find_subseq(s)  # Find end-point of subsequence
            if not end:
                break

            start = improve_subseq(end)  # Improve start-point of subsequence

            if debug:
                print(f"\nWindow candidate: S[{start}:{end + 1}] = {S[start:end + 1]} (len={end - start + 1})")

            if end - start + 1 < min_len:
                min_len = end - start + 1
                min_window = S[start:end + 1]
                if debug:
                    print(f"  New min window found: '{min_window}'")

            s = start + 1  # Start next subsequence search
            if debug:
                print(f"New s: {s}")
                print(f"--" * 30)

        if debug:
            print(f"\nFinal result: {min_window}")
        return min_window



s1 = 'abacbcdfeg'
s2 = 'bcde'
print(Solution().minWindow(s1=s1, s2=s2))
