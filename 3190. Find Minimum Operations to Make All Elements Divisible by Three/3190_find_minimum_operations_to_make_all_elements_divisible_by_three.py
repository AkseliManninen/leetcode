# Runtime 40 ms

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum([0 if n % 3 == 0 else 1 for n in nums])
        