# my-leetcode

## Daily Coding Challenge February 2024

### February 1 : 2966. Divide Array Into Arrays With Max Difference

1. Sort `nums`
2. Compare two elements to check if they satifsy max difference `k`.<br>Append to `res`.

```python
for i in range(0,n,3):
            if nums[i+1]-nums[i] > k or nums[i+2]-nums[i+1] > k or nums[i+2]-nums[i] > k:
                return []
            res.append([nums[i],nums[i+1],nums[i+2]])
```

3. TC : O(nlogn) - because sorting <br>SC : O(n) - `res` 

### February 2 : 1291. Sequential Digits 

1. Generate all the sequential digits within the given constraints
```python
seq = []
s = '123456789'
for i in range(9):
    for j in range(i+2,10):
        seq.append(int(s[i:j]))
```
2. Sort `seq`
3. Compute all `num` within the [`low`,`high`] range
```python
for num in seq:
    if num >= low and num <= high:
        res.append(num)
```
4. TC : O(36) - maximum number of sequential digits in this case is 36<br>SC : O(36) - `seq`

### February 3 : 1043. Partition Array for Maximum Sum

#### Dynamic Programming : Front Partition
<br>Recursion<br>

1. Define `f(ind)` where `ind` is index of `arr`
2. Base Case
```py
if ind == n:
    return 0
```
3. Front Partition<br>Increase `len` of partition. <br>Find `maxi` = maximum element in partition so far<br>Compute `sum`.<br>Recursive call to next index.<br>Update `res`
```py
res = 0
len, maxi = 0, float("-infinity")
for j in range(ind, min(n,ind+k)):
    len += 1
    maxi = max(maxi,arr[j])
    sum = len*maxi + f(j+1)
    res = max(res,sum)
```

Memoize<br>

1. Define `dp`
```py
dp = [-1 for _ in range(n)]
```
2. Check if `dp[i]` already computed
```py
if dp[ind] != -1:
    return dp[ind]
```
3. Update `dp` and return
```py
dp[ind] = res
return dp[ind]
```

Finally call `f(0)` for result

### February 4 : 76. Minimum Window Substring
#### Sliding Window
1. Count characters of `t`
```py
for ch in t:
    countT[ch] = 1 + countT.get(ch,0)
```
2. `l` and `r` pointers
```py
l = 0
for r in range(len(s)):
```
3. Shift `r` and count characters in window
```py
for r in range(len(s)):
    ch = s[r]
    countWindow[ch] = 1 + countWindow.get(ch,0)
```
4. Find a match
```py
if ch in countT and countWindow[ch] == countT[ch]:
    match += 1
```
5. Shift `l` to minimize window when we find substring
```py
while match == lenT:
    # update result
    if (r - l + 1) < resLen:
        res = [l,r]
        resLen = r - l + 1
    # shrink window
    countWindow[s[l]] -= 1
    if s[l] in countT and countWindow[s[l]] < countT[s[l]]:
        match -= 1
    l += 1
```

Finally return `s[l : r + 1]`

### February 5 : 387. First Unique Character in a String

1. Count character occurence of `s`
```py
count = {}
for ch in s:
    count[ch] = 1 + count.get(ch,0)
```
2. Return `i` of first character unique character (`count[s[i]]==1`)
```py
for i in range(len(s)):
    if count[s[i]] == 1:
        return i
``` 
3. Return `-1` if no unique characters

### February 6 : 49. Group Anagrams

1. To find anagrams, compare the sorted string
2. To group them, use default dictionary with `tuple(str)` as key and `list` of `s` as value
```py
res = defaultdict(list)
for s in strs:
    res[tuple(sorted(s))].append(s) 
```
3. Return `res.values()`

### February 7 : 451. Sort Characters By Frequency

1. Count freqency of characters
```py
count = {}
for ch in s:
    count[ch] = 1 + count.get(ch,0)
```
2. Sort the dictionary by value in decreasing order
```py
count = sorted(count.items(), key=lambda x:x[1], reverse = True)
```
3. Iterate through the dictionary and create `res` by appending `ch`, `mul` times, where `mul` is the frequency
```py
res = ""
for ch,mul in count:
    res = res + ch*mul
```

### February 8 : 279. Perfect Squares

1. Initialize the `dp` array
```py
dp = [-1 for _ in range(n+1)]
```
2. Recursive function `f(n)`
3. Base Case : 

```python
if n==0:                                                    
    return 0  
```
- `n == 0` , no squares are needed to sum up to zero.

4. Memoization check
```py
if dp[n] != -1:
    return dp[n]
```
5. Main logic
```py
mini = n                                                     
i = 1
while i*i<=n:                                               
    mini = min(mini, f(n-(i*i)))
    i+=1
dp[n] =  mini+1                                              
return dp[n]
```
- `mini` is initialized to `n`, assuming the worst case where the sum consists of `n` 1's (1<sup>2</sup> + 1<sup>2</sup> + ... + 1<sup>2</sup>)
- loop through all square numbers less than `n`
- add `1` to account for the square number used in this step

Finally, call and return `f(n)`

### February 9 : 368. Largest Divisible Subset

1. Sort `nums` 
2. Initialize the `dp` dictionary
3. Recursive function `f(n)`
4. Base Case : 

```python
if ind<0:
    return []
```
- `n < 0` , out of bounds case

5. Memoization check
```py
if (ind,prev) in dp:
    return dp[(ind,prev)]
```
6. Main logic
```py
res = f(ind-1,prev)
if prev == 1 or prev % nums[ind] == 0:
    pick = [nums[ind]] + f(ind-1,nums[ind])
    if len(pick) > len(res):
        res = pick

dp[(ind,prev)] = res
return res
```

Finally, call and return `f(len(nums)-1,1)`

