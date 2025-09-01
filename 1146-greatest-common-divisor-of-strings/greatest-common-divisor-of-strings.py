class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = len(str1)
        m= len(str2)
        if str1 + str2 != str2+ str1 :
            return ""
        gcd_l = math.gcd(n,m)
        return(str2[:gcd_l]) 
            