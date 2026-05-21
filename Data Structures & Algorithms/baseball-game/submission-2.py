class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            print(i)
            if i == "+":
                x = stack[-1] + stack[-2]
                stack.append(x)
            elif i == "D":
                x = stack.pop()
                y = x * 2
                stack.append(x)
                stack.append(y)
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))
            print(stack)
            
        # print(stack)
        return sum(stack)