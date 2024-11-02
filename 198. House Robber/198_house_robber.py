# Runtime complexity: O(n)
# Memory complexity O(1)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev2, prev1 = 0, nums[0]

        for i in range(1, len(nums)):
            current = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current
        
        return prev1