# Runtime 40 ms

class Solution:
    def compress(self, chars):
        left, right = 0, 0 

        while right < len(chars):
            char = chars[right]
            count = 0
            while right < len(chars) and chars[right] == char:
                right += 1
                count += 1
            
            chars[left] = char
            left += 1

            if count > 1:
                for num in str(count):
                    chars[left] = num
                    left += 1
        return left