# !!!not tested yet
#
# Jincheng Zhang 1/26/2017
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
#
# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
#
# Would this affect the run-time complexity? How and why?
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Write a function to determine if a given target is in the array.
#
# The array may contain duplicates.
#
#
# Time  O(n)
# Space O(1)
# hint: binary search with a turning point, linear search when list is not growing


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l != r:
            m = int((l+r)/2)
            if target == nums[m]:
                return m
            if nums[m] > nums[l]:
                if target < nums[m] and target >= nums[l]:
                    r = m
                else:
                    l = m+1
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m+1
                else:
                    r = m
        if target == nums[l]:
            return l
        return -1


##for debugging
sol = Solution()
list = [4,5,6,7,0,1,2]
print(sol.search(list, 6))
print(list[sol.search(list, 6)])
