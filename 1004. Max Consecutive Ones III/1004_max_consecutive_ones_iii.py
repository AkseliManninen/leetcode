# Runtime 67 ms

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        l = 0
        count = 0
        switch = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                switch += 1

            while switch > k:
                if nums[l] == 0:
                    switch -= 1
                l += 1

            count = max(count, r - l + 1)

        return count
        