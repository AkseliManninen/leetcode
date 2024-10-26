class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        r = sum(nums)    

        for i, _ in enumerate(nums):
            r -= nums[i]
            if l == r:
                return i
            l += nums[i]  
        return -1