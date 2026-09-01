class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #key is closing bracket, value is opening
        closeToOpen = {')': '(', '}':'{', ']':'['}

        for c in s:
            if c in closeToOpen:
                #if c is in closeToOpen that means its a closing bracket
                #stack cannot be empty if we find a closing bracket
                if stack and stack[-1] == closeToOpen[c]:
                    #notice we never add the closing bracket to the stack
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False




            
            
            
        
        