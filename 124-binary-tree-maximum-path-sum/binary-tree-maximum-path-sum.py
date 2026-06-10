# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_val = float("-inf")

        def dfs(node):
            #base condition
            if not node:
                return 0

            left_val = max(0, dfs(node.left))
            right_val = max(0, dfs(node.right))

            self.max_path_val = max(self.max_path_val,node.val + left_val + right_val )
            return max( node.val+ left_val, node.val + right_val)
            
        dfs(root)
        return  self.max_path_val














        # self.max_path_sum = float("-inf")
        # def dfs(node):
        #     #base condition
        #     if not node:
        #         return 0

        #     left_sum = dfs(node.left)
        #     right_sum = dfs(node.right)

        #     self.max_path_sum = max(self.max_path_sum, node.val, left_sum + node.val, right_sum+node.val, node.val + right_sum+ left_sum )            
        #     return max(node.val, left_sum + node.val, right_sum+node.val )

        # dfs(root)
        # return self.max_path_sum
        