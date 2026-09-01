class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        f={}
        seen=set()
        for x in arr:
            f[x]=f.get(x,0)+1
        for x in f.values():
            
            if x in seen:
                return False
            else:
                seen.add(x)
        return True