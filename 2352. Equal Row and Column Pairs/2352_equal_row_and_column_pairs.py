# Time complexity: O(n^3)
# Space complexity: O(n^2)

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        res = 0
        for col in list(zip(*grid)):
            for row in grid:
                if list(col) == row:
                    res += 1
        
        return res

        