# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])

        while q:
            level=[]
            for _ in range(len(q)):
                element = q.popleft()
                level.append(element.val)
                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)
            res.append(level)
        return res
        