class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=stones
        for i in range(len(heap)):
            heap[i] = -heap[i]
        heapq.heapify(heap)
        while(len(heap)>1):
            y=heapq.heappop(heap)
            x=heapq.heappop(heap)
            if x!=y:
                heapq.heappush(heap,y-x)
        if len(heap)==0:
            return 0
        else:
            return -heapq.heappop(heap)