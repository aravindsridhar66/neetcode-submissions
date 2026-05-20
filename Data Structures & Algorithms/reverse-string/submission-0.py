class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            s1 = s[i]
            s2 = s[j]
            s[i] = s2
            s[j] = s1
            i+=1
            j-=1
        