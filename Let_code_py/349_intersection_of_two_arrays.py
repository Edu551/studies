class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))
    
    def intersection_hash(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hash_set = {}
        res = []
        for n in nums1:
            if n not in hash_set:
                hash_set[n] = 0
            else:
                continue

        for n in hash_set:
            if n in nums2:
                res.append(n)

        return res


s = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(s.intersection_hash(nums1, nums2))
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(s.intersection_hash(nums1, nums2))
