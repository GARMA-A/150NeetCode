class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == "[" or ch == "(" or ch == "{":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                else:
                    top = stack.pop()
                if ch == "]" and top == "[":
                    continue
                elif ch == ")" and top == "(":
                    continue
                elif ch == "}" and top == "{":
                    continue
                else:
                    return False

        return True if len(stack) == 0 else False


s = Solution()
print(s.isValid("({[]}})"))
