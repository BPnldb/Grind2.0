class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = list(nums)
        for i in nums:
            res.append(i)
        return res