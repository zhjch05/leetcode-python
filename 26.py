#Jincheng Zhang 1/25/2017
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        index = 0
        for i in range(1, len(nums)):
            if nums[index] != nums[i]:
                index+=1
                nums[index] = nums[i]
        del nums[index+1:]
        return index+1



##for debugging
sol = Solution()
list = [1,1,2,3,4,4,4,4,4,5,5,5,6]
print(sol.removeDuplicates(list))
print(list)
