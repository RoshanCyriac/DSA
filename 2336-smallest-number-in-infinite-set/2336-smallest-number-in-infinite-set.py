import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.next_num = 1
        self.heap = []
        self.seen = set()

    def popSmallest(self):
        if self.heap:
            num = heapq.heappop(self.heap)
            self.seen.remove(num)
            return num

        num = self.next_num
        self.next_num += 1
        return num

    def addBack(self, num):
        if num < self.next_num and num not in self.seen:
            heapq.heappush(self.heap, num)
            self.seen.add(num)