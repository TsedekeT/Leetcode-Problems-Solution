class Solution:
    def minimizedStringLength(self, s: str) -> int:

        # Using a set to track distinct characters in the string
        distinct_chars = set(s)
        return len(distinct_chars)

