class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        letterOccurence = {}

        for letter in s:
            letterOccurence[letter] = letterOccurence.get(letter, 0) + 1

        for letter in t:
            if letterOccurence.get(letter) == None:
                return False
            else :
                letterOccurence[letter] -= 1 

        for occurence in letterOccurence.values():
            if occurence != 0:
                return False

        return True