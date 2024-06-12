class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index=1
        n=len(nums)
        temp=nums[0]
        for i in range(n):
            if temp!= nums[i]:
                temp=nums[i]
                nums[index]=nums[i]
                index+=1
        return index
