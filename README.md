# my-leetcode

### Daily Coding Challenge February 2024

#### February 1 : 2966. Divide Array Into Arrays With Max Difference

1. Sort `nums`
2. Compare two elements to check if they satifsy max difference `k`.<br>Append to `res`.

```python
for i in range(0,n,3):
            if nums[i+1]-nums[i] > k or nums[i+2]-nums[i+1] > k or nums[i+2]-nums[i] > k:
                return []
            res.append([nums[i],nums[i+1],nums[i+2]])
```

3. TC : O(nlogn) - because sorting <br>SC : O(n) - `res` 

#### February 2 : 1291. Sequential Digits 

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

#### February 3 : 1043. Partition Array for Maximum Sum

Dynamic Programming : Front Partition<br>Recursion<br>

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