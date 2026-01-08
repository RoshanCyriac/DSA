class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        small=0
        capital=0
        if word[0].isupper():
            for i in range(len(word)):
                if word[i].islower():
                    small+=1
                elif word[i].isupper():
                    capital+=1
            if capital==len(word):
                return True
            elif small==len(word)-1:
                return True
            else:
                return False
        else:
            for i in range(len(word)):
                if word[i].islower():
                    small+=1
                elif word[i].isupper():
                    capital+=1
            if small==len(word):
                return True
            else:
                return False


        
         