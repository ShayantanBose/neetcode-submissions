class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        arr = []
        for num, freq in count.items():
            arr.append([freq, num])
        arr.sort()

        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        return res

                