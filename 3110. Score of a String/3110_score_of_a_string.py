# Time complexity: O(n)
# Space complecity: O(n)

class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_values = [ord(c) for c in s]
        
        score = 0
        i, j = 0, 1
        while j < len(ascii_values):
            score += abs(ascii_values[i] - ascii_values[j])
            i += 1
            j += 1

        return score 