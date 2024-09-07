class Solution:
    def removeStars(self, s: str) -> str:
        stack = [] # s = "leet**cod*e" 
        for i in range(len(s)):
            if s[i].isalnum():
                stack.append(s[i])
            elif s[i] == '*':
                stack.pop()
        return ("").join(stack)
