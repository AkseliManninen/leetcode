# Runtime 4197 ms, beats 5%

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(len(nums)):
            num = nums[i]
            nums2 = list(nums)
            nums2.remove(num)
            if num not in nums2:
                return num