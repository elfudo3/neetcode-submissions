class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):  
            if tokens[i] == '+' and stack:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b + a)
            elif tokens[i] == '-' and stack:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b - a)
            elif tokens[i] == '*' and stack:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b * a)
            elif tokens[i] == '/' and stack:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(int(b / a))
            else:
                stack.append(int(tokens[i]))
        return stack[-1]
        
        

            
