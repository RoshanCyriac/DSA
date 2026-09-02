class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node, maximum):
            nonlocal ans

            if not node:
                return

            if node.val >= maximum:
                ans += 1

            maximum = max(maximum, node.val)

            dfs(node.left, maximum)
            dfs(node.right, maximum)

        dfs(root, root.val)

        return ans