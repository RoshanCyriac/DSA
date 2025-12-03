class Solution:
    def findMaxConsecutiveOnes(self, nums):
        best = 0
        current = 0
        
        for x in nums:
            if x == 1:
                current += 1
                if current > best:
                    best = current
            else:
                current = 0
        
        return best
