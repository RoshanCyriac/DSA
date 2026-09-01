class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        right=0
        left=0
        nz=0
        ans=0
        l=0
        for x in nums:
            if x==0:
                nz+=1
            if nz<k+1:
                right+=1
            elif nz>=k+1:
                
                while nz>=k+1:                    
                    if nums[left]==0:
                        nz-=1
                    left+=1
                right+=1   
            l=right-left
            ans=max(l,ans)       
        return ans
        
