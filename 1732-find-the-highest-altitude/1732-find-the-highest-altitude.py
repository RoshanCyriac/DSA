class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        f={0:0}
        n=len(gain)
        # f[1]=gain[0]+0
        for x in range(1,n+1):
            f[x]=f.get(x-1,0)+gain[x-1]
        ans=max(f.values())
        return ans