class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        max_power = 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
                max_power = max(max_power, count) # (2, 3) = 3
            else:
                count = 1
        return max_power
        # s = "abbcccddddeeeeedcba"  i = 5 >> c == d
