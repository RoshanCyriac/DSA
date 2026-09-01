from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        f1 = Counter(word1)
        f2 = Counter(word2)

        if set(f1.keys()) != set(f2.keys()):
            return False

        if sorted(f1.values()) != sorted(f2.values()):
            return False

        return True