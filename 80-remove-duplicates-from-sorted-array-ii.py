# Jincheng Zhang 1/25/2017
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
#
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
#
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
#
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
#
# Time  O(n)
# Space O(1)
# hint: add a counter "toggle" to count twice


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        index = 0
        toggle = True
        for i in range(1, len(nums)):
            if nums[index] != nums[i]:
                index+=1
                nums[index] = nums[i]
                toggle = True
            elif toggle:
                index+=1
                nums[index] = nums[i]
                toggle = False
        del nums[index+1:]
        return index+1

##for debugging
sol = Solution()
list = [1,1,2,3,4,4,4,4,4,5,5,5,6]
print(sol.removeDuplicates(list))
print(list)
