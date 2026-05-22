class Solution:
    START = ['(', '[', '{']
    MAP = { ')': '(', ']': '[', '}': '{'}
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in self.START:
                stack.append(c)
            else:
                if not stack:
                    return False
                x = stack.pop()
                if x != self.MAP[c]:
                    return False
                
        
        if not stack:
            return True
        else: 
            return False
            
        