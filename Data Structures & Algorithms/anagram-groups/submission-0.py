class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            count = [0] * 26 # a - z lowercase

            for c in s:
                val = ord(c) - ord('a')
                count[val] += 1
            key = tuple(count)
            if key in res:
                res[key] += [s]
            else:
                res[key] = [s]

        solution = []
        # print(res)
        for i in res:
            solution += [res[i]]

        return solution
