class Solution:
    def magicalSum(self, m: int, k: int, nums):
        MOD = 10**9 + 7
        n = len(nums)

        # precompute powers
        powv = [[1]*(m+1) for _ in range(n)]
        for i in range(n):
            for c in range(1, m+1):
                powv[i][c] = powv[i][c-1] * nums[i] % MOD

        # precompute combinations
        C = [[0]*(m+1) for _ in range(m+1)]
        for i in range(m+1):
            C[i][0] = C[i][i] = 1
            for j in range(1, i):
                C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD

        @lru_cache(None)
        def dfs(i, used, carry, bits):
            # reached end of indices
            if i == n:
                # process remaining carry bits
                b = bits + carry.bit_count()
                return 1 if (used == m and b == k) else 0

            res = 0

            # try picking this index "take" times
            for take in range(m - used + 1):

                total = carry + take
                bit = total & 1
                newCarry = total >> 1

                newBits = bits + bit
                if newBits > k:
                    break

                ways = (
                    C[m-used][take] *
                    powv[i][take] %
                    MOD
                )

                res += ways * dfs(i+1, used+take, newCarry, newBits)
                res %= MOD

            return res

        return dfs(0, 0, 0, 0)

        
    # def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
    #     output = 0
    #     n = len(nums)
    #     # if m > n:
    #     #     return output 

    #     MOD = 10**9 + 7        
    #     #used = [False] * n
    #     prems = []   
   
    #     @lru_cache(None)
    #     # def dfs(input):
    #     def dfs(cnt, mask):
    #         nonlocal output

    #         #if len(input) == m:
    #         if len(input) == m:
    #             product = 1
    #             set_bit = 0
    #             #print([input])
    #             for j in input:
    #                 set_bit += 2**j
    #                 product *= nums[j]

    #             if set_bit.bit_count() == k:
    #                 return product % MOD
                    
    #                 #return [input]
    #             else:
    #                 return 0
           
            
    #         res = 0
    #         for i in range(n):
    #             #if not used[i]:
    #                 #used[i] = True
    #                 res += dfs(input + (i,))
    #                 res %= MOD
    #                 #used[i] = False
    #         return res

    #     return dfs(())

        #print(dfs([]))
        # perms = dfs([])
        # #print(len(perms))
        
        # for perm in perms:            
        #     product = 1
        #     set_bit = 0
        #     for i in perm:
        #         set_bit += 2**i
        #         product *= nums[i]

        #     if set_bit.bit_count() == k:
        #         output += product 
        #         output %= MOD
 
        # return output     

        