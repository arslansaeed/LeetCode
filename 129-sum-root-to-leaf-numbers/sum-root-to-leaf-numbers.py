# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        def dfs(node, local_sum):
            # base condition
            if not node:
                return

            if not node.left and not node.right:                
                self.sum += int(local_sum + str(node.val))  
                return     

            local_sum = local_sum + str(node.val)   
            dfs(node.left, local_sum)
            dfs(node.right, local_sum)

        dfs(root, "")
        return self.sum
        
        