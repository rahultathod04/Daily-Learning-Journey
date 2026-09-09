# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        if root is None:
            return TreeNode(val)
        
        curr = root
        while True:
            if (curr.val > val): # move to left
                if(curr.left is None):
                    curr.left = TreeNode(val)
                    break
                else:
                    curr = curr.left
            else:
                if(curr.right is None):
                    curr.right = TreeNode(val)
                    break
                else:
                    curr = curr.right

        return root
            
        