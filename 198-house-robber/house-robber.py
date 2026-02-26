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
    def rob_tabulation(self, nums: List[int]) -> int:
        n  = len(nums)

        prev1 , prev2 = 0, 0
        for num in nums:
            curr = max(num + prev2, prev1)
            prev2 =prev1
            prev1 = curr

        return prev1

    def rob(self, nums: List[int]) -> int:
        n  = len(nums)
        memo ={}
       
        def dfs(idx: int):
            if idx >=  n:
                return 0

            if idx in memo:
                return memo[idx] 

            robbed = nums[idx] + dfs(idx + 2)
            skipped  = dfs(idx + 1)

            maxi = max(robbed, skipped)
            memo[idx] = maxi

            return maxi

        return dfs(0)




        

            
           

        