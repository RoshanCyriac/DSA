class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeated = a
        count = 1
        
        # Keep repeating until length >= b
        while len(repeated) < len(b):
            repeated += a
            count += 1
        
        # Check if b is now a substring
        if b in repeated:
            return count
        
        # One more repetition for overlap cases
        repeated += a
        count += 1
        
        if b in repeated:
            return count
        
        return -1
