class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # keep count of t
        # sliding window
        # r -> shift to find matches
        # match == len(countT)
        # l -> shift to make minimum window 
        
        countT, countWindow = {}, {}
        for ch in t:
            countT[ch] = 1 + countT.get(ch,0)
        lenT = len(countT)
        
        res, resLen = [-1,-1], float("infinity")
        match = 0
        l = 0
        for r in range(len(s)):
            ch = s[r]
            countWindow[ch] = 1 + countWindow.get(ch,0)

            # checkpoint to find a match
            if ch in countT and countWindow[ch] == countT[ch]:
                match += 1

            # checkpoint to shrink window
            while match == lenT:
                # update result
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = r - l + 1
                # shift window if possible
                countWindow[s[l]] -= 1
                if s[l] in countT and countWindow[s[l]] < countT[s[l]]:
                    match -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""