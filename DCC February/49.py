class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # find anagrams : sort(str)
        # group them : {str:list}

        res = defaultdict(list)
        for s in strs:
            res[tuple(sorted(s))].append(s)

        return res.values() 