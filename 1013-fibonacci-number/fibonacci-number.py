# fab(n) is n+1 element in fab serious if starting from 0 index
# fibonacci serious starting from 0 -   0, 1,1,2,3,5,8    if we start from 0 then for n=6  we need to go n+1 = 7 
# finoacci serious starting from 1         1,1,2,3,5,8    if we start from 1 then for n= 6 we need to go to n = 6

class Solution:
    # solved using recurssion
    def fib_recur(self, n: int) -> int:
        if n <= 1:
            return n

        return self.fib(n-1) + self.fib(n-2)
        
    # solved using sliding window
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        pre, curr = 0, 1
        for i in range (2, n + 1):
            pre ,  curr = curr, curr+pre

        return curr 

    # solved using tabulation - bottom up dp
    def fib_tabulation(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp [i-1] + dp[i -2]

        return dp[n]
