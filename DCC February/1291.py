class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # 12 -> 89 == 8
        # 123 -> 789 == 7
        # 1234 -> 6789 == 6
        #
        #
        #
        # 123456789 == 1
        # we need a string 123456789, to generate all sequential digits
        seq = []
        s = '123456789'
        for i in range(9):
            for j in range(i+2,10):
                seq.append(int(s[i:j]))
        seq = sorted(seq)
        print(len(seq))
        res = []
        for num in seq:
            if num >= low and num <= high:
                res.append(num)

        return res