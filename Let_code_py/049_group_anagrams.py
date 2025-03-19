class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]: # O(n * k * log(k))
        if len(strs) <= 1:
            return [strs]
        
        strsDict = {}

        for str in strs:
            str_ordered = "".join(sorted(str))

            strsDict.setdefault(str_ordered, []).append(str) # simpler
            # if str_ordered in strsDict:
            #     strsDict[str_ordered].append(str)
            # else:
            #     strsDict[str_ordered] = [str]

        return list(strsDict.values())
                
s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))