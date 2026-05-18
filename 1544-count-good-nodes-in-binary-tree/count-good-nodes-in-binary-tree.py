# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #self.count = 0

        def dfs(node, cur_max):
            # base confition
            if not node:
                return 0

            
            if cur_max <= node.val:
                cur_max =  node.val
                count = 1
            else:
                count  = 0


            count += dfs(node.left, cur_max)
            count += dfs(node.right, cur_max)

            return count

        return dfs(root, root.val)

        