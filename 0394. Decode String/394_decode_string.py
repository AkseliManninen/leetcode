# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def decodeString(self, s: str) -> str:
        
        current_str = ""
        current_k = ""
        stack = []
        
        i = 0
        while i < len(s):
            if s[i].isdigit():
                current_k += s[i]
            elif s[i] == "[":
                stack.append(current_str)
                stack.append(current_k)
                current_str = ""
                current_k = ""
            elif s[i] == "]":
                previous_k = int(stack.pop())
                previous_str = stack.pop()
                current_str = previous_str + previous_k * current_str
            # alphabet
            else:
                current_str += s[i]
            i += 1
        
        return current_str

            


        