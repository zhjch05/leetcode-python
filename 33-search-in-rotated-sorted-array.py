# Jincheng Zhang 1/25/2017
# https://leetcode.com/problems/search-in-rotated-sorted-array/
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
#
#
# Time  O(log(n))
# Space O(1)
# hint: binary search with a turning point


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
            if nums[m] >= nums[l]:
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
