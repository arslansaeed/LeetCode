class Solution:
    # time out
    def rob_dfs(self, nums: List[int]) -> int:
        n  = len(nums)
        if n == 1:
            return nums[0]
           
        def dfs(i: int, end: int):
            if i > end:
                return 0

            robbed =  nums[i] + dfs(i+2, end)
            skipped = dfs(i+1 , end)

            return max(robbed, skipped)
        
        return max(dfs(0, n-2), dfs(1, n-1))     


    def rob(self, nums: List[int]) -> int:
        n  = len(nums)
        if n == 1:
            return nums[0]
           
        def dfs(i: int, end: int, memo: dict):
            if i > end:
                return 0

            if i in memo:
                return memo[i]

            robbed =  nums[i] + dfs(i+2, end, memo)
            skipped = dfs(i+1 , end, memo)

            max_val = max(robbed, skipped)
            memo[i] = max_val

            return max_val

        
        return max(dfs(0, n-2, {}), dfs(1, n-1, {}))     