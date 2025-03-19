class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freqDict = {}
        for num in nums:
            if num in freqDict:
                freqDict[num] += 1
            else:
                freqDict[num] = 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in freqDict.items():
            buckets[freq].append(num)
        
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
                
s = Solution()
arr = [1,1,1,2,2,3,3,3,3,4,4,5]
k = 2
print(s.topKFrequent(arr, k))