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