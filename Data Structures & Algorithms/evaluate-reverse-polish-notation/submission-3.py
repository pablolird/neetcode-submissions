class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in "*+-/":
                stack.append(int(t))
                continue
            
            v = stack.pop()
            if t=="+":
                stack[-1]+=v
            elif t=="-":
                stack[-1]-=v
            elif t=="/":
                stack[-1]= int(stack[-1]/v)
            elif t=="*":
                stack[-1]*=v
        
        return stack[0]

