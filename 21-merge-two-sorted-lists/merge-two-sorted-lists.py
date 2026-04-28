# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1

        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
























    def mergeTwoLists_with_loop(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        list3 = cur = ListNode()
        if not list1:
            return list2
        
        if not list2:
            return list1
       
        while list1 and list2:
            if list1.val <= list2.val:
                list3.next = list1               
                list1 = list1.next
            else:
                list3.next = list2      
                list2 = list2.next

            list3 = list3.next

        list3.next = list1 if list1 else list2

        return cur.next

    def mergeTwoLists_old(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if not list1:
            return list2
        
        if not list2:
            return list1
       
       
        if list1.val <= list2.val:               
           
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:                   
           
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
         

     

        return head