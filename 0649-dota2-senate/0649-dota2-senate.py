from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R = deque()
        D = deque()

        for i in range(len(senate)):
            if senate[i] == 'R':
                R.append(i)
            else:
                D.append(i)

        n = len(senate)

        while R and D:
            r = R.popleft()
            d = D.popleft()

            if r < d:
                R.append(r + n)
            else:
                D.append(d + n)

        if R:
            return "Radiant"
        else:
            return "Dire"