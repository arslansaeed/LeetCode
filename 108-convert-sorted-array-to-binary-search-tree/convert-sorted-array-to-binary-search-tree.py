# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(start, end):
            #base condition
            if start > end:
                return None

            mid  = (start + end )// 2
            root = TreeNode(nums[mid])
            root.left = dfs(start, mid -1)
            root.right = dfs(mid+ 1, end)

            return root

        return dfs(0,len(nums) -1)





















    # def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

    #     def recursion ( l, r):
    #         #base case
    #         if l > r:
    #             return 

    #         mid  = (l+r)//2
    #         root  = TreeNode(nums[mid])
    #         root.left = recursion(l, mid -1)
    #         root.right = recursion(mid+1, r)

    #         return root

    #    #print(len(nums)-1)
    #     return recursion(0,len(nums)-1)




        