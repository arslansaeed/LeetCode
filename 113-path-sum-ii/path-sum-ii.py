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
            #path1 = path[:] 
            path.append(node.val)
            local_sum  += node.val

          
            if (not node.left) and (not node.right):
                if local_sum == targetSum:
                    output.append(path[:])
                    #output.append(path)
                    # we can remove below 2 line and let it run line 26,27 and do pop as
                    # return at line 12-13 will run quickly that solution is also fine
                    # path.pop()
                    # return
                    
            dfs(node.left, local_sum,path)            
            dfs(node.right, local_sum,path)

            path.pop()

            #return local_sum
        
        dfs(root, 0,[])
 
        return output

