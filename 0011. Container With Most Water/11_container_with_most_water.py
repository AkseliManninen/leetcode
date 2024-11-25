# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height)-1
        
        max_water = min(height[left], height[right]) * (right-left) # height x width

        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            max_water = max((min(height[left], height[right]) * (right-left)), max_water)
        return max_water