# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:    
    def hasCycle(self, head: Optional[ListNode]) -> bool: 
        if not head:
            return False  

        node_set = {head}     
        while head.next:
            if head.next in node_set:
                return True
            node_set.add(head.next)
            head = head.next

        return False
            




        