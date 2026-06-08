"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.isLeaf = isLeaf
                #If the current grid has different values, set isLeaf to False
        self.val = val   # 1,0 
                # True if the node represents a grid of 1's or False if the node represents a grid of 0's       
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def dfs(size, startx,starty):
            #base condition
            leaf = True
            
            first_Val = grid[startx][starty]
            for i in range(size):
                for j in range(size):
                    if first_Val != grid[startx+i][starty+j]:
                        leaf = False
                        break;
                if not leaf:
                    break

            if leaf:
                return Node(first_Val, True, None, None,None,None)
          
            node = Node()
            node.isLeaf = leaf
            node.val = 1 if leaf else first_Val

            half = size//2 
            node.topLeft = dfs(half, startx,starty)
            node.topRight = dfs(half, startx,starty+half)
            node.bottomLeft = dfs(half, startx+half,starty)
            node.bottomRight = dfs(half, startx+half,starty+half)

            return node

        return dfs(n,0,0)
