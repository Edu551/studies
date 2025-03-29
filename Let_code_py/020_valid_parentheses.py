class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        
        stack = []
        open_brackets= {"(" : ")", "[" : "]", "{" : "}"}

        for bracket in s:
            if bracket in open_brackets:
                stack.append(open_brackets[bracket])
            elif not stack or bracket != stack.pop():
                return False
            
        return not stack

so = Solution()
# s = "()"
# s = "()[]{}"
# s = "(]"
# s = "([])"
s = "){"
print(so.isValid(s))