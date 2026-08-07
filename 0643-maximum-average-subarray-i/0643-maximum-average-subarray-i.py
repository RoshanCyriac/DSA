class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        first=0
        last=k-1
        n=len(nums)
        ans=sum(nums[:k])
        temp=ans
        for i in range(k,n):
            last=i
            temp=temp+nums[last]-nums[first]
            first+=1
            ans=max(ans,temp)
        avg=ans/k
        return avg

        