class Solution:
    def twoSum_hash_map(self, nums: list[int], target: int) -> list[int]: # O(n)
        if len(nums) <= 0:
            return nums
        
        tempDict = {}
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in tempDict:
                return [tempDict[complement], i]
            
            tempDict[nums[i]] = i

        return []

s = Solution()
target = 9
nums = [2,7,11,15]

print(s.twoSum_hash_map(nums, target))