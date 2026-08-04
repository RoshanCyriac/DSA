class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        result=[]
        n=len(words)
        
        for i in range(n-1,-1,-1):
            result.append(words[i])
        ans=" ".join(result)
        return ans