class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # init a stack 
        for i in range(len(s)):
            if stack:
                last = stack[-1]
                if self.is_pair(last, s[i]):
                    stack.pop()
                    continue
            stack.append(s[i])

        return not stack

    def is_pair(self, last, cur):
        if (
            last == "("
            and cur == ")"
            or last == "["
            and cur == "]"
            or last == "{"
            and cur == "}"
        ):
            return True
        return False
