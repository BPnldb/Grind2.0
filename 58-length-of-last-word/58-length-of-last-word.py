class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        print(s)
        newS = s.strip()
        newS = newS.split(' ')
        res = []
        for i in newS:
            if i is not ' ':
                res.append(i)
        return len(res[-1])