# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia  = 0

        def dfs(node):
            #nonlocal dia
            if not node:
                return 0
            
            left_height =dfs(node.left)
            right_height = dfs(node.right)
            t_height = left_height + right_height
            if t_height > self.dia:
                self.dia = t_height
            return 1 + max(left_height , right_height)



        dfs(root)
        return self.dia




















    def diameterOfBinaryTree_hamza(self, root: Optional[TreeNode]) -> int:
        output = 0

        def dfs(node):
            nonlocal output

            if not node:
                return 0
            
            r_left = dfs(node.left) 
            r_right = dfs(node.right) 
            dia = r_left + r_right
            if  dia > output:
                output = dia  
            return 1+ max(r_left,r_right)
            
        dfs(root)
        return output