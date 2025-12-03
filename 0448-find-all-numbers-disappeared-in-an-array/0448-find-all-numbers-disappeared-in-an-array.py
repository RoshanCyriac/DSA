class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for x in nums:
            value = abs(x)-1
            if nums[value]>0:
                    nums[value]=-nums[value]
        result=[]
        for i in range(n):
            if nums[i]>0:
                result.append(i+1)
        return result




            