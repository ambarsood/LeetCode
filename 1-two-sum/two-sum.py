class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        length = len(nums)

        for i in range(length):
            complement = target-nums[i]
            if complement in numMap:
                return [numMap[complement],i]
            numMap[nums[i]]=i
