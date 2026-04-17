class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        wordLetterOccurence = defaultdict(list)

        for word in strs:

            letterOccurence = [0] * 26

            for letter in word:
                letterOccurence[ord(letter) - 97] += 1
            
            wordLetterOccurence[tuple(letterOccurence)].append(word)

        return list(wordLetterOccurence.values())




        

