# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
            
        root = TreeNode(postorder[len(postorder) - 1])
        root_index = inorder.index(postorder[len(postorder)-1])
        
        root.left = self.buildTree(inorder[0:root_index], postorder[0:root_index])
        root.right = self.buildTree(inorder[root_index + 1:len(inorder)], postorder[root_index:len(postorder)-1])
        return root