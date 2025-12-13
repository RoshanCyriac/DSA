class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []  # will store indices
        res = prices[:]  # copy of original prices

        for i in range(len(prices)):
            # find discount for earlier items
            while stack and prices[i] <= prices[stack[-1]]:
                idx = stack.pop()
                res[idx] -= prices[i]
            
            stack.append(i)

        return res
