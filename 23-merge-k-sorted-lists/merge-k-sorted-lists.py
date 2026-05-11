# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #print(lists)
       
        if not lists:
            return None

        n = len(lists)
        if n < 2:
            return lists[0]

        def merge2(cl, cr):
            if not cl:
                return cr

            elif not cr:
                return cl

            if cl.val <= cr.val:
                cl.next = merge2(cl.next, cr)
                return cl
            elif cl.val > cr.val:
                cr.next = merge2(cr.next,cl)
                return cr
        

        def merge(output, r):
            #base case            
            if r >= n:
                return output
            
            output  = merge2(output, lists[r])  
            #print(output)          
            return merge(output,r+1)                 

        return merge(lists[0] ,1)