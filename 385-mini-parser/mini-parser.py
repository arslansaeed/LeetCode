# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize_iterative(self, s: str) -> NestedInteger:
        stack = []       
        num =""

        if s[0] != "[":
            return NestedInteger(int(s))

        for ch in s:
            if ch == "[":
                stack.append(NestedInteger())              
                 
            elif ch == "]":
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num =""

                temp = stack.pop()

                if stack:
                    stack[-1].add(temp)
                else:   
                    return temp

            elif ch == ",": 
                if num:               
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""

            else:
                num += ch

    def deserialize(self, s: str) -> NestedInteger:     
        num =""

        if s[0] != "[":
            return NestedInteger(int(s))

        n = len(s)
        def dfs(i, nestedInteger, num):  
            #base condition
            if i > n-1:
                return nestedInteger, i

            ch = s[i]

            if ch == "[":
                # stack.append(NestedInteger())  
                next_list, next_i =  dfs(i+1 , NestedInteger(), "")   
              
                if nestedInteger:
                    nestedInteger.add(next_list)  
             
                return dfs(next_i  , nestedInteger, "")  

            elif ch == "]":             
                if num:    
                    nestedInteger.add(NestedInteger(int(num)))
                    num = ""
                
                return nestedInteger, i+1  
               
            elif ch == ",": 
                if num:               
                    nestedInteger.add(NestedInteger(int(num)))
                    num = ""

                return  dfs(i+1, nestedInteger, num)   
                                
            else:
                num += ch
                return dfs(i+1, nestedInteger, num) 
              

          

        result, _ = dfs(1, NestedInteger(), "")
        return result



     
