class Solution:
    def firstUniqChar(self, s: str) -> int:
        # first pass to count occurence
        # second pass to get index
        count = {}
        for ch in s:
            count[ch] = 1 + count.get(ch,0)
        
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        
        return -1