class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        count=0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index += 1
                count=0
            elif nums[i]==nums[i-1]:
                if count<1:
                    count+=1
                    nums[index] = nums[i]
                    index += 1

        return index