class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length

c = Solution()
s = "abcabcbb"
d = "dvdt"

print(c.length_of_longest_substring(s))
print(c.length_of_longest_substring(d))