# Time complexity: O(n log(m))
# Space complexity: O(1)

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        l, r = 1, max(piles)

        def pile_takes_hours(pile, pivot):
            if pile % pivot == 0:
                return pile // pivot
            else:
                return pile // pivot + 1

        while l < r:
            pivot = (l + r) // 2
            eats_hours = sum(pile_takes_hours(pile, pivot) for pile in piles)
            if eats_hours > h:
                l = pivot + 1
            else:
                r = pivot
        return l
            
            