class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        output = []
        def dfs(curr, opened,closed):
            # base condition
            if len(curr) == 2*n:
                output.append(curr)               
                return

            if opened < n:       
                dfs(curr + "(", opened +1, closed)

            if closed < opened:
                dfs(curr + ")", opened , closed +1)


        dfs("", 0, 0 )
        return output