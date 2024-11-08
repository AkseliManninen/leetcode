# Time complexity: O(log n)
# Space complexity: O(1)

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l, r = 0, len(nums) - 1
    
        while l < r:
            pivot = (l + r) // 2
            if nums[pivot] < nums[pivot + 1]:
                l = pivot + 1
            else:
                r = pivot
        
        return l
        
        