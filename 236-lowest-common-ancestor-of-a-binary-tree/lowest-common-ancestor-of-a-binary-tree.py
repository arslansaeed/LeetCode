# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return 

        if root == p or root == q:
            return root

        l_node = self.lowestCommonAncestor(root.left, p, q)
        r_node = self.lowestCommonAncestor(root.right, p, q)

        if l_node and not r_node:
            return l_node

        if r_node and not l_node:
            return r_node
        
        if l_node and r_node:
            return root





        
        