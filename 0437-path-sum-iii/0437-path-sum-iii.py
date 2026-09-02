class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def findPaths(node, target):
            if not node:
                return 0

            count = 0

            if node.val == target:
                count += 1

            count += findPaths(node.left, target - node.val)
            count += findPaths(node.right, target - node.val)

            return count

        if not root:
            return 0

        return (findPaths(root, targetSum)
                + self.pathSum(root.left, targetSum)
                + self.pathSum(root.right, targetSum))