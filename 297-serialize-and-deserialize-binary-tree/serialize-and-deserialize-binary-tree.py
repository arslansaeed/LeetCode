# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.serialize_string  = ""
        def dfs(node):
            #base condition
            if not node:
                if self.serialize_string == "": 
                    self.serialize_string +=  "null"
                else:
                    self.serialize_string += ",null"
                return 

            if self.serialize_string == "": 
                self.serialize_string +=  str(node.val)    
            else:
                self.serialize_string += "," + str(node.val)     

            dfs(node.left)          
            dfs(node.right)


        dfs(root)   
        #print(self.serialize_string) 
        return self.serialize_string
    
    # def serialize(self, root):
    #     values = []

    #     def dfs(node):
    #         if not node:
    #             values.append("null")
    #             return

    #         values.append(str(node.val))
    #         dfs(node.left)
    #         dfs(node.right)

    #     dfs(root)
    #     return ",".join(values)
        

    def deserialize(self, data):
    #     """Decodes your encoded data to tree.
        
    #     :type data: str
    #     :rtype: TreeNode
    #     """
        node_val = data.split(',')      

        def dfs(i):    
            if node_val[i] == "null":
                return (None, i)

            node  = TreeNode(int(node_val[i]))
            node.left, i = dfs(i+1)
            node.right, i = dfs(i+1)

            return (node,i)

        return dfs(0)[0]

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))