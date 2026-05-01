# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced  = True

        def dfs(node):
            nonlocal balanced
            #base case
            if not node:
                return 0

            height_left = dfs(node.left)
            height_right = dfs(node.right)

            diff = abs(height_left - height_right)
            if diff > 1:
                balanced  = False

            return max(height_left, height_right) +1

        dfs(root)
        return balanced


        