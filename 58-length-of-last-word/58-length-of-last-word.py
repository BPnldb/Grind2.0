class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        print(s)
        newS = s.strip().split(' ')
        newS = list(newS)
        print(newS)
        return len(newS[-1])