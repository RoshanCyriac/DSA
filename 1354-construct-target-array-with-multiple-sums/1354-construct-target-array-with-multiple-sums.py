import heapq
from typing import List

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # max heap using negatives
        heap = [-x for x in target]
        heapq.heapify(heap)

        total = sum(target)

        while True:
            max_val = -heapq.heappop(heap)
            rest = total - max_val

            # base case: all ones
            if max_val == 1 or rest == 1:
                return True

            # impossible cases
            if rest == 0 or max_val <= rest:
                return False

            # reverse the operation
            old = max_val % rest
            if old == 0:
                return False

            # update
            heapq.heappush(heap, -old)
            total = rest + old
