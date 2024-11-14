# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        after = []
        
        for asteroid in asteroids:
            while after and asteroid < 0 < after[-1]:
                if after[-1] < -asteroid:
                    after.pop()
                    continue
                elif after[-1] == -asteroid:
                    after.pop()
                break
            else:
                after.append(asteroid)
        
        return after
