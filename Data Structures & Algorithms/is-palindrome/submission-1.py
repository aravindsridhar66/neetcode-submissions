import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(s)
        start = 0
        end = len(s) - 1
        while start != end and start < end:
            if s[start] != s[end]:
                print(s[start])
                print(s[end])
                return False
            
            start += 1
            end -= 1
        
        return True