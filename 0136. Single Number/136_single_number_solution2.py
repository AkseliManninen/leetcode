# Runtime 0 ms, beats 100%

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        unique_num = 0

        for num in nums:
            unique_num ^= num
        return unique_num
