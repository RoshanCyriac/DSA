# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        node1=root1
        node2=root2
        arr1=[]
        arr2=[]
        def inorder(abc,arr):
            
            if not abc:
                return
            inorder(abc.left,arr)
            inorder(abc.right,arr)
            if abc.left==None and abc.right==None:
                arr.append(abc.val)
            
        inorder(root1,arr1)
        inorder(root2,arr2)
        if arr1==arr2:
            return True
        else:
            return False