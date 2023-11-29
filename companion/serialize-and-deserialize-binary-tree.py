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
        def encode(node):
            if not node:
                return "null"
            return str(node.val) + "," + encode(node.left) + "," + encode(node.right)
        return encode(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def decode(values):
            if values[0] == "null":
                values.pop(0)
                return None
            root = TreeNode(int(values[0]))
            values.pop(0)
            root.left = decode(values)
            root.right = decode(values)
            return root
        values = data.split(",")
        return decode(values)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))