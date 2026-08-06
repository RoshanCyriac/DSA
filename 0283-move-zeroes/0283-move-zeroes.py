class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        n=len(nums)
        j=0
        count=0
        temp=[]
        for i in range(n):
            if nums[i]!=0:
                temp.append(nums[i])
            
        t=len(temp)
        for i in range(n-t):
            temp.append(0)
        nums[:]=temp
                


        