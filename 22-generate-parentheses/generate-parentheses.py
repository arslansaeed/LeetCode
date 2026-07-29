class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        output = []
        def dfs(curr, opened,closed):
            # base condition
            if len(curr) == 2*n:
                output.append(curr) 
                #print(f"in base condition curr is {curr}")              
                return

            if opened < n:       
                dfs(curr + "(", opened +1, closed)

            #print(f"after opened dfs curr is {curr}") 
            if closed < opened:
                dfs(curr + ")", opened , closed +1)
            #print(f"after closed dfs curr is {curr}") 


        dfs("", 0, 0 )
        return output