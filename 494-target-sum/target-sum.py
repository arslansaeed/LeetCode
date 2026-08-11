class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
       
        dp = {}
        l = len(nums)

        def dfs(idx, curr_sum):
           
            #base condition
            if idx == l:
                if curr_sum == target:
                    return 1
                return 0
            
            if (idx, curr_sum) in dp:
                return dp[(idx, curr_sum)]

            addi_sum = dfs(idx+1, curr_sum + nums[idx]) 
            sub_sum = dfs(idx+1, curr_sum - nums[idx])

            dp[(idx, curr_sum)] = addi_sum + sub_sum

            return dp[(idx, curr_sum)]

        return dfs(0,0)
       
        