# 42 ms

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(1 if l in jewels else 0 for l in stones)