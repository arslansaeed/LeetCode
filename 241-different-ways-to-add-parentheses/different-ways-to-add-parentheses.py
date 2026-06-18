# class Solution:
#     def diffWaysToCompute(self, expression: str) -> List[int]:

#         self.result = []
#         def dfs(expression):
           
#             if expression.isdigit():
#                 return int(expression)

#             result_val = 0
#             for i, ch in enumerate(expression):
                
#                 if ch in "+-*":
#                     # left_expression = expression[:i]
#                     # right_expression = expression[i + 1:]

#                     left_result = dfs(expression[:i])
#                     right_result = dfs(expression[i + 1:])
#                     if ch == "+":
#                         result_val  = left_result + right_result
#                     elif ch == "-":
#                         result_val  = left_result - right_result
#                     else:
#                         result_val  = left_result * right_result

#                     #print(result_val)
#                     return result_val
#                 #print(f"out of loop :{result_val}")
#                 self.result.append(result_val)

#         dfs(expression)
#         return self.result

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        def dfs(expression):
            # Base condition
            if expression.isdigit():
                return [int(expression)]

            result = []

            for i, ch in enumerate(expression):

                if ch in "+-*":
                    left_results = dfs(expression[:i])
                    right_results = dfs(expression[i + 1:])

                    for left_result in left_results:
                        for right_result in right_results:

                            if ch == "+":
                                result_val = left_result + right_result
                            elif ch == "-":
                                result_val = left_result - right_result
                            else:
                                result_val = left_result * right_result

                            result.append(result_val)

            return result

        return dfs(expression)




