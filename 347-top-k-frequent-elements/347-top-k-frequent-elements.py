class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count ={}
        freq = [[] for i in range(len(nums)+ 1)]
        
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i],0)
        # {1:3, 2:2, 3:1}
        
        for i, c in count.items():
            freq[c].append(i)
        print(freq)
        
        res = []
        
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res