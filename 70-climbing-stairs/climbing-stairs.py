class Solution:
    def climbStairs(self, n: int) -> int:

        dp = {}

        def dfs(rem_steps):
           

            # base condition
            if rem_steps == 0:              
                return 1
            
            if rem_steps < 0:
                return 0

            if rem_steps in dp:
                return dp[rem_steps]

            dp[rem_steps] = dfs(rem_steps -1) +  dfs(rem_steps -2)
            return dp[rem_steps]
                

        return dfs(n)
   
