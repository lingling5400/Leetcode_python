class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)): #不能重複，所以要從i+1開始
                if(nums[i]+nums[j]==target):
                    return [i,j]

        return [-1,-1]
