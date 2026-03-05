class Solution:
    def maxProduct_our(self, nums: List[int]) -> int:
        n = len(nums)
        r_pro = 1
        output = float('-inf')

        for num in nums:
            r_pro = max(num, r_pro * num)
            output = max(output, r_pro)

        return output

    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        r_pro = 1
        output = nums[0]

        for i in range(1, n):
            r_pro = max(nums[i], r_pro * num[i])
            output = max(output, r_pro)

        return output
        

















































    def maxProduct(self, nums: List[int]) -> int:
        ln = len(nums)
        mn = mx  = result =  nums[0]

        for i in range(1, ln):
            if nums[i] < 0:
                mn, mx  = mx, mn

            mn = min(mn * nums[i], nums[i])
            mx = max(mx * nums[i], nums[i])

            result = max(result, mx)

        return result

        
    def maxProduct_brute(self, nums: List[int]) -> int:
        ln = len(nums)
        mx = float('-inf')

        for i in range(ln):
            prod = 1
            print(f"curent value of {i}")
            for j in range(i,ln):
                prod  = prod * nums[j]
                mx = max(mx , prod)
                print(mx)


        return mx