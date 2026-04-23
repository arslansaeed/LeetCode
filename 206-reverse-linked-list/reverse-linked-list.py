# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        curr = head
        next_node  = None
        prev = None
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


        

        

        

























    def reverseList_old(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        cur = head       
        prev = None

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node       
                 
        return prev