class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        
        result = []
        count = 0
        
        for i in range(len(s) - 1, -1, -1):
            result.append(s[i])
            count += 1
            
            if count == k:
                result.append('-')
                count = 0
        
        # remove trailing dash if present
        if result and result[-1] == '-':
            result.pop()
        
        return ''.join(result[::-1])
        
            

        