class Solution:
    # with db -memorization
    def rob_dp(self, nums: List[int]) -> int:
        n  = len(nums)
        memo = {}

        def dfs(idx: int):
            if idx >=  n:
                return 0

            if idx in memo:
                return memo[idx]

            robbed = nums[idx] + dfs(idx +2)
            skipped  = dfs(idx+1)

            max_robb = max(robbed, skipped)
            memo[idx] = max_robb

            return max_robb   

        return dfs(0)

    # time out with out dp
    def rob_dfs(self, nums: List[int]) -> int:
        n  = len(nums)
       
        def dfs(idx: int):
            if idx >=  n:
                return 0
            
            robbed = nums[idx] + dfs(idx +2)
            skipped  = dfs(idx+1)

            return max(robbed, skipped)

        return dfs(0)

    # dfs with tabulation
    def rob(self, nums: List[int]) -> int:
        n  = len(nums)

        prev1 , prev2 = 0, 0
        for num in nums:
            curr = max(num + prev2, prev1)
            prev2 =prev1
            prev1 = curr

        return prev1



    # def rob(self, nums: List[int]) -> int:
    #     n  = len(nums)
    #     output  = 0

    #     def dfs(idx: int, amount: int):
    #         nonlocal output

    #         #print(f"idx: {idx}")
    #         if idx > n-1:
    #             print(f"amount: {amount}, output:{output}")
    #             output = max(output, amount)
    #             return

    #         amount += nums[idx]
    #         #print(f"amount: {amount}")
    #         for i in range(idx+2, n+2):                
    #             dfs(i, amount)

        
    #     dfs(0,0)
    #     dfs(1,0)

    #     return output
            

        

            
           

        