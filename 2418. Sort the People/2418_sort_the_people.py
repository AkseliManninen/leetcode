# Time complexity: Average O(n log n), Worst case O(n^2)
# Space complexity: O(n)

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        heights_and_names = list(zip(heights, names))

        def quick_sort(heights_and_names):
            if len(heights_and_names) <= 1:
                return heights_and_names

            pivot_idx = len(heights_and_names) // 2
            pivot = heights_and_names[pivot_idx]

            right = [x for x in heights_and_names if x[0] > pivot[0]]
            middle = [x for x in heights_and_names if x[0] == pivot[0]]
            left = [x for x in heights_and_names if x[0] < pivot[0]]

            return quick_sort(right) + middle + quick_sort(left)
        
        sorted_heights, sorted_names = list(zip(*quick_sort(heights_and_names)))

        return sorted_names
            