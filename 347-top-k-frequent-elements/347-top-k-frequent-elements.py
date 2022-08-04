class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        freq = [[] for i in range(len(nums) + 1)] #list of list
        print(freq)
        for i in nums:
            count[i] = 1 + count.get(i,0)
        
        for i, c in count.items():
            freq[c].append(i)
            
        res = []
        
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
               
        