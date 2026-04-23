class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paranthesis = {
            ')': '(',
            '}' : '{',
            ']' :'['
            }

        for i in range(len(s)):
            if s[i] not in paranthesis:
                stack.append(s[i])        

            elif len(stack) > 0 and paranthesis[s[i]] == stack[-1]:
                stack.pop() 
            else:
                return False

        return len(stack) == 0


        