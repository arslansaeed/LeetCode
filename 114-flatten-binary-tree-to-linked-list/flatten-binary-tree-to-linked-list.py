# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        #base condition
        if not root:
            return 

        l_node = self.flatten(root.left)
        r_node = self.flatten(root.right)

        #swap
        #if node.right:
        temp = root.right
        root.right = root.left
        root.left = None

        tail = root
        while tail.right:
            tail = tail.right

        tail.right = temp

        return root
    



    def flatten_old(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            #base condition
            if not root:
                return

            dfs(root.left)
            dfs(root.right)

            temp  = root.right
            root.right = root.left
            root.left = None

            tail = root
            while tail.right:
                tail = tail.right

            tail.right  = temp
            return root

        return dfs(root)














        # def dfs(r_node):
        #     # base case
        #     if not r_node:
        #         return 

        #     temp = r_node.right
        #     r_node.right = r_node.left
        #     r_node.left  = None

        #     tail = dfs(r_node.right)

        #     if temp:
        #         tail.right = temp
        #         tail = tail.right
        #          dfs(r_node.right)

        #     return tail

        # dfs(root, None)
            
    
