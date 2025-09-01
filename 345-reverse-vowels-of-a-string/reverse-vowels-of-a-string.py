class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        st = list(s)
        left, right = 0, len(st) - 1

        while left < right:
            if st[left] not in vowels:
                left += 1
            elif st[right] not in vowels:
                right -= 1
            else:
                st[left], st[right] = st[right], st[left]
                left += 1
                right -= 1

        return "".join(st)
