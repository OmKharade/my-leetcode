# my-leetcode

### Daily Coding Challenge February 2024

February 1 :
2966. Divide Array Into Arrays With Max Difference

1. Sort `nums`
2. 

```python
for i in range(0,n,3):
            if nums[i+1]-nums[i] > k or nums[i+2]-nums[i+1] > k or nums[i+2]-nums[i] > k:
                return []
            res.append([nums[i],nums[i+1],nums[i+2]])
```

3. TC : O(nlogn) - because sorting <br>SC : O(n) - `res` 