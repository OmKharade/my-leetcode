class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        for ch in s:
            count[ch] = 1 + count.get(ch,0)
        count = sorted(count.items(), key=lambda x:x[1], reverse = True)
        res = ""
        for ch,mul in count:
            res = res + ch*mul

        return res