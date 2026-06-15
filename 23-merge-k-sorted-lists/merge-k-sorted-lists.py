# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:   
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def dfs(a,b):
            if not a:
                return b
            
            elif not b:
                return a

            else:
                #curr = a
                if a.val <= b.val:
                    a.next = dfs(a.next,b)
                    return a
                else:
                    b.next = dfs(a,b.next)
                    return b


        n  = len(lists)
        if n == 0:
            return None
        elif n <2:
            return lists[0]
       
        output = lists[0]
        for i in range(1,n):
            output = dfs(output, lists[i])

        return output


   


            




     

        