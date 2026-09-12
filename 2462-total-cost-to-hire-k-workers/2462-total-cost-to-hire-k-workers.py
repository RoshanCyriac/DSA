import heapq
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)

        left_heap = []
        right_heap = []

        left = 0
        right = n - 1

        # Fill the initial hiring windows
        for _ in range(candidates):
            if left > right:
                break
            heapq.heappush(left_heap, (costs[left], left))
            left += 1

        for _ in range(candidates):
            if left > right:
                break
            heapq.heappush(right_heap, (costs[right], right))
            right -= 1

        total = 0

        for _ in range(k):
            if not right_heap or (
                left_heap and left_heap[0] <= right_heap[0]
            ):
                cost, index = heapq.heappop(left_heap)
                if left <= right:
                    heapq.heappush(
                        left_heap, (costs[left], left)
                    )
                    left += 1
            else:
                cost, index = heapq.heappop(right_heap)
                if left <= right:
                    heapq.heappush(
                        right_heap, (costs[right], right)
                    )
                    right -= 1

            total += cost

        return total