# Runtime 117 ms

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        l, r = 0, 0

        while r < len(nums)-1:
            r += 1
            if nums[l] == 0:
                if nums[r] != 0:
                    nums[l] = nums[r]
                    nums[r] = 0
                    l += 1
            else:
                l = r
        return nums