class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurence = {}

        for num in nums:
            if occurence.get(num) == None:
                occurence[num] = 1
            else:
                occurence[num] += 1

            if occurence[num] > 1:
                return True
        
        return False