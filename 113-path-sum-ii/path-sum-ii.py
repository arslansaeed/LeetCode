# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []
        #curr_path = list()

        def dfs(node: Optional[TreeNode], local_sum, path):
            if not node:                
                return 
            

            path.append(node.val)
           

            local_sum  += node.val
            dfs(node.left, local_sum,path[:])
            if (not node.left) and (not node.right):
                if local_sum == targetSum:
                    output.append(path[:])
                    

            else:
                dfs(node.right, local_sum,path[:])

            return local_sum
        
        dfs(root, 0,[])
 
        return output

    