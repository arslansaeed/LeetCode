# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return root.val

        self.pathsum = float("-inf")

        def dfs(node):
            if not node:
                return 0
            
            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right) ,0)

            t_sum = left_sum + right_sum + node.val
            if t_sum > self.pathsum:
                self.pathsum = t_sum 
            # elif node.val > self.pathsum:
            #     self.pathsum  = node.val
            # max_child = max(left_sum, right_sum)
            # return max(max_child + node.val , node.val)
            return max(left_sum, right_sum) + node.val

        dfs(root)
        return self.pathsum