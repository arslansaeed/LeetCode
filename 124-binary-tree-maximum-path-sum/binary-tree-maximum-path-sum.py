# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum  = float('-inf')
         
        def dfs(root):
            if not root:
                return 0
            
            l_val  = max(0, dfs(root.left))
            r_val = max(0 , dfs(root.right))

            self.max_sum = max(self.max_sum, root.val + l_val + r_val )
            return max( root.val + l_val, root.val + r_val)

        dfs(root)
        return self.max_sum


    def maxPathSum_first_attempt(self, root: Optional[TreeNode]) -> int:
        self.max_sum  = float('-inf')
         
        def dfs(root):
            if not root:
                return 0
            
            l_val  = dfs(root.left)
            r_val = dfs(root.right)

            c_l_val = root.val + l_val
            c_r_val = root.val + r_val

            self.max_sum = max(self.max_sum, root.val, root.val + l_val + r_val, root.val + l_val,  root.val + r_val  )
            return max( root.val + l_val, root.val + r_val, root.val )

        dfs(root)
        return self.max_sum






















    # def maxPathSum(self, root: Optional[TreeNode]) -> int:
    #     if not root.left and not root.right:
    #         return root.val

    #     self.pathsum = float("-inf")

    #     def dfs(node):
    #         if not node:
    #             return 0
            
    #         left_sum = max(dfs(node.left), 0)
    #         right_sum = max(dfs(node.right) ,0)

    #         t_sum = left_sum + right_sum + node.val
    #         if t_sum > self.pathsum:
    #             self.pathsum = t_sum 

    #         return max(left_sum, right_sum) + node.val

    #     dfs(root)
    #     return self.pathsum