# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dic = {0 : 1}

        def dfs(node, cur_sum):
            #base condition
            if not node:
                return 0

            cur_sum  += node.val
            if (cur_sum - targetSum) in dic and  dic[cur_sum - targetSum] > 0:
                count = dic[cur_sum - targetSum]
            else:
                count =0

            if cur_sum in dic:
                dic[cur_sum] += 1
            else:
                dic[cur_sum] = 1

            count += dfs(node.left, cur_sum)
            count += dfs(node.right, cur_sum)

            dic[cur_sum] -= 1

            return count

        return dfs(root, 0)

            

































    def pathSum_ours(self, root: Optional[TreeNode], targetSum: int) -> int:
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