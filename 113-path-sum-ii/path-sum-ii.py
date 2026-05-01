# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []

        def dfs(node: Optional[TreeNode], local_sum, path):
            if not node:                
                return 
            
            path.append(node.val)
            local_sum  += node.val

          
            if (not node.left) and (not node.right):
                if local_sum == targetSum:
                    output.append(path[:])
                    
            dfs(node.left, local_sum,path)            
            dfs(node.right, local_sum,path)

            path.pop()

            #return local_sum
        
        dfs(root, 0,[])
 
        return output


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        output = []

        def dfs(node, current_sum, path):

            if not node:
                return

            # choose
            path.append(node.val)
            current_sum += node.val

            # leaf node
            if not node.left and not node.right:
                if current_sum == targetSum:
                    output.append(path[:])

            # explore
            dfs(node.left, current_sum, path)
            dfs(node.right, current_sum, path)

            # un-choose (backtrack)
            path.pop()

        dfs(root, 0, [])

        return output