class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        letterOccurence = {}

        for letter in s:
            if letterOccurence.get(letter) == None:
                letterOccurence[letter] = 1
            else :
                letterOccurence[letter] += 1

        for letter in t:
            if letterOccurence.get(letter) == None:
                return False
            else :
                letterOccurence[letter] -= 1 

        for letter, occurence in letterOccurence.items():
            if occurence != 0:
                return False

        return True