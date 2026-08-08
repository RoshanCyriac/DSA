class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        first=0
        last=k
        n=len(s)
        ans=0
        for i in range(first,last):
             if s[i] in ["a","e","i","o","u"]:
                    count+=1
        ans=count
        for j in range(k,n):
            if s[j] in ["a","e","i","o","u"] and s[first] not in ["a","e","i","o","u"]:
                count+=1
            elif s[j] not in ["a","e","i","o","u"] and s[first] in ["a","e","i","o","u"]:
                count-=1
            ans=max(count,ans)
            first+=1
            last+=1
        return ans