class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        maxHeap = [-i for i in nums]
        heapq.heapify(maxHeap)
        if len(maxHeap) < 3:
            return (-maxHeap[0])
        else:
            heapq.heappop(maxHeap)
            heapq.heappop(maxHeap)
            return -maxHeap[0]