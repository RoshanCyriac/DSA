# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node, left, right):
            nonlocal ans

            if not node:
                return

            ans = max(ans, left, right)

            # Go LEFT → next direction must be RIGHT
            if node.left:
                dfs(node.left, right + 1, 0)

            # Go RIGHT → next direction must be LEFT
            if node.right:
                dfs(node.right, 0, left + 1)

        dfs(root, 0, 0)
        return ans