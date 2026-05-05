# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def dfs(node):
            if not node:
                return 

            dfs(node.left)
            output.append(node.val)
            dfs(node.right)

        dfs(root)
        return output
    
    
    
    def inorderTraversal_recurssive(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)


        inorder(root)
        return result      
        

    def inorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root

        while curr or stack:

            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

       
        return result      

    #Morris Preorder Traversal
    def inorderTraversal_(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        curr = root

        while curr:
            if not curr.left:
                result.append(curr.val)
                curr = curr.right
            else:
                #predecessor
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right

                if not pred.right:
                    pred.right = curr
                    curr = curr.left

                else:
                    pred.right = None
                    result.append(curr.val)
                    curr = curr.right          

       
        return result   