class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: split by spaces (handles multiple spaces too)
        words = s.split()

        # Step 2: reverse the list of words
        words.reverse()

        # Step 3: join back with a single space
        return " ".join(words)
