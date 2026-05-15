# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # we need to keep track of min and max vlaue at each node
        # we go to the bottom and then come back - keeping track of max, min 
        self.max_dif = 0

        def dfs(node):
            if not node:
                return [float("-inf"), float("+inf")]                

            l_max, l_min = dfs(node.left)
            r_max, r_min = dfs(node.right)


            if l_min != float("+inf") or r_min != float("+inf"):
                self.max_dif =  max( self.max_dif , abs(min(l_min,r_min) - node.val), abs(max(l_max, r_max)- node.val))


            n_max = max(l_max,r_max, node.val)
            n_min = min(l_min, r_min, node.val)


            return [n_max, n_min]
        
        dfs(root)
        return self.max_dif