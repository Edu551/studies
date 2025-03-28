class Solution:
    def containsDuplicate_shorting(self, nums: list[int]) -> bool: # O(n log n)
        nums.sort()
        index = 0
        while index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                    return True
            index += 1
        
        return False
    
    def containsDuplicate_hash_map(self, nums: list[int]) -> bool: # O(n)
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = 1

        return False
    
    def hasDuplicate(self, nums: list[int]) -> bool: # O(n)
        return len(nums) != len(set(nums))
        
        
s = Solution()
nums = [1,2,3,1]
nums_2 = [1,2,3,5]
# print(s.containsDuplicate_shorting(nums))
# print(s.containsDuplicate_shorting(nums_2))
print(s.containsDuplicate_hash_map(nums))
print(s.containsDuplicate_hash_map(nums_2))