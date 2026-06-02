# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def dfs(root):
            #base condition
            if not root:               
                return None
            
            if not root.next:
               return TreeNode(root.val)

            slow = root
            fast = root
            #temp = ListNode()
            temp = None
            print(f"before while")
          
            #calculate mid
            while fast and fast.next:
                temp = slow
                slow = slow.next
                fast = fast.next.next               

            temp.next = None
            node  =  TreeNode(slow.val)
            print(node.val)

            node.left = dfs(root)
            node.right = dfs(slow.next)
            

            return node

        return dfs(head)