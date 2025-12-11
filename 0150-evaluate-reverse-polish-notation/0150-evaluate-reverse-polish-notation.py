class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        def trunc_div(a, b):
            # Division that truncates toward zero
            sign = -1 if a * b < 0 else 1
            return sign * (abs(a) // abs(b))
        
        for tok in tokens:
            if tok in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                
                if tok == "+":
                    stack.append(a + b)
                elif tok == "-":
                    stack.append(a - b)
                elif tok == "*":
                    stack.append(a * b)
                else:  # division
                    stack.append(trunc_div(a, b))
            
            else:
                stack.append(int(tok))
        
        return stack[-1]
