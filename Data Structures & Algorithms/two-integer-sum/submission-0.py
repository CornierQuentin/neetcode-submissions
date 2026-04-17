class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        substractionResult = {}

        for numIndex in range(len(nums)):
            
            if substractionResult.get(nums[numIndex]) != None:
                return [substractionResult[nums[numIndex]], numIndex]
            else:
                substractionResult[target - nums[numIndex]] = numIndex