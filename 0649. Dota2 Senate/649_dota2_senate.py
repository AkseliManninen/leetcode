# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        r_queue = []
        d_queue = []

        for i,x in enumerate(senate):
            if x == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)

        n = len(senate)

        while r_queue and d_queue:
            r_i = r_queue.pop(0)
            d_i = d_queue.pop(0)

            if r_i < d_i:
                r_queue.append(r_i+n)
            else:
               d_queue.append(d_i+n)
        
        return "Radiant" if r_queue else "Dire"
