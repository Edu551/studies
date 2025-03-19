class Solution:
    def isAnagram_sorted(self, s: str, t: str) -> bool: # O(n log n)
        if  (len(s) != len(t)):
            return False
        return sorted(s) == sorted(t)
    
    def isAnagram_hashmap(self, s: str, t: str) -> bool: # 	O(n)
        if (len(s) != len(t)):
            return False
        # return Counter(s) == Counter(t) --> from collections import Counter
        
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for char in t:
            if char not in freq or freq[char] == 0:
                return False
            freq[char] -= 1
        
        return all(count == 0 for count in freq.values())
            

    

s = Solution()
# print(s.isAnagram_sorted("anagram", "nagaram"))
# print(s.isAnagram_sorted("anagramm", "nagaram"))
# print(s.isAnagram_sorted("rat", "car"))

print(s.isAnagram_hashmap("anagram", "nagaram"))
print(s.isAnagram_hashmap("anagramm", "nagaram"))
print(s.isAnagram_hashmap("rat", "car"))