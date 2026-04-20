class Solution:
    def runningSum_iterative(self, nums: List[int]) -> List[int]:

        for i in range (1, len(nums)):
            nums[i] += nums[i-1]

        return nums

    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        def recursion(idx = 1):
            if idx == n:
                return 
            nums[idx] += nums[idx -1]                       
            recursion(idx + 1)

        recursion()
        return nums