class Solution:
    def jump(self, nums: List[int]) -> int:
       N=len(nums)
       i,jump,lastpos,maxpos=0,0,0,0

       while i<N-1:

        maxpos=max(maxpos,i+nums[i])
        if i==lastpos:
            lastpos=maxpos
            jump+=1
        i+=1
       return jump 
