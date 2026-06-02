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
          
            #calculate mid
            while fast and fast.next:
                temp = slow
                slow = slow.next
                fast = fast.next.next               

            temp.next = None
            node  =  TreeNode(slow.val)           

            node.left = dfs(root)
            node.right = dfs(slow.next)            

            return node

        return dfs(head)

    def sortedListToBST_chat(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Count length of linked list
        size = 0
        curr = head

        while curr:
            size += 1
            curr = curr.next

        self.head = head

        def build_tree(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            mid = (left + right) // 2

            # Build left subtree first
            left_child = build_tree(left, mid - 1)

            # Current linked list node becomes root
            root = TreeNode(self.head.val)
            root.left = left_child

            # Move linked list pointer forward
            self.head = self.head.next

            # Build right subtree
            root.right = build_tree(mid + 1, right)

            return root

        return build_tree(0, size - 1)