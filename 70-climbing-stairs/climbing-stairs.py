class Solution:
    # def climbStairs(self, n: int) -> int:
    #     count  = 0
        
    #     def backtrack(num: int):
    #         nonlocal count
    #         if num == 0:
    #             count += 1
    #             return                

    #         if num < 0:
    #             return

    #         backtrack(num -1)
    #         backtrack(num - 2)

    #     backtrack(n)
    #     return count

    
    def climbStairs(self, n: int) -> int:
        #count  = 0
        
        @lru_cache(None)
        def backtrack(num: int):
            #nonlocal count
            if num == 0:
                return 1               

            if num < 0:
                return 0

           
            return backtrack(num -1) + backtrack(num - 2)
            

        return backtrack(n)


    