# Jincheng Zhang 1/25/2017
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
#
#
#
# Time  O(n)
# Space O(1)


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
