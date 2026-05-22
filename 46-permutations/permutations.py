class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used  = [False] * n
        output = []
        path = []

        def backtracking():
            if len(path) == n:
                output.append(path[:])
                return

            for i in range(n):
                if used[i]:
                    continue

                #chose
                used[i] = True
                path.append(nums[i])
                
                backtracking()
                
                #undo choice
                path.pop()
                used[i] = False

                

             
        backtracking()
        return output