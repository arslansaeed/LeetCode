# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = []
        def dfs(node, path):
            # base condition
            if not node:
                return

            if not node.left and not node.right:                
                output.append(path + str(node.val))  
                return     

            path = path + str(node.val) + "->"  
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return output
        