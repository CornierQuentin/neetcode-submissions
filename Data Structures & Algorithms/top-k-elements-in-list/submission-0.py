class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numberOccurence = defaultdict(int)

        n = len(nums)

        for num in nums:
            numberOccurence[num] += 1

        numberByOccurence = [[] for _ in range(n + 1)]

        for num, occurence in numberOccurence.items():
            numberByOccurence[occurence].append(num)

        result = []
        numberToFind = k

        for index in range(n, -1, -1):

            for num in numberByOccurence[index]:
                result.append(num)
                numberToFind -= 1

                if numberToFind <= 0:
                    return result
        
