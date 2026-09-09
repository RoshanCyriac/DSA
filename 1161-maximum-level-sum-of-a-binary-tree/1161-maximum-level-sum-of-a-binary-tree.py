from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        que = deque([root])

        count = 1
        ans = root.val
        c = 1

        while que:
            n = len(que)
            sums = 0

            for i in range(n):
                node = que.popleft()

                sums += node.val

                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)

            if sums > ans:
                ans = sums
                c = count

            count += 1

        return c