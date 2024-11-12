# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def removeStars(self, s: str) -> str:
        queue = []
        
        for c in s:
            if c == "*":
                queue.pop(-1)
            else:
                queue.append(c)
        
        return "".join(queue)