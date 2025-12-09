class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s=[]
        output=[]
        cur=1
        for i in target:
            while cur<i:
                output.append("Push")
                output.append("Pop")
                cur+=1
            output.append("Push")
            cur+=1
        return output