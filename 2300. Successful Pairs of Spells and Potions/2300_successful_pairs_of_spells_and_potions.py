# Time complexity: O((n+m) log m)
# Space complexity: O(n)

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        

        potions.sort()
        counts = []
        duplicates = {}

        for spell in spells:
            if spell in duplicates:
                counts.append(duplicates[spell])
            
            else:
                l, r = 0, len(potions)
                while l < r:
                    pivot = (l + r) // 2
                    if potions[pivot] * spell >= success:
                        r = pivot
                    else:
                        l = pivot + 1
                count = len(potions) - l
                counts.append(count)
                duplicates[spell] = count

        return counts
            

        