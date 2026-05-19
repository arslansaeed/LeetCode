# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.counter  = 0

        def dfs(node, path):
            #base condition
            if not node:
                return 

            path.append(node.val)

            dfs(node.left, path)
            dfs(node.right, path)
            
            sum = 0
            for i in range(len(path) -1, -1, -1 ):
                sum += path[i]
                if sum == targetSum:
                    self.counter += 1

            path.pop()



        dfs(root, [])
        return self.counter