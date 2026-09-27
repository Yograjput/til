
arr = [1, 2, 4, 7, 11, 15]
target = 15

left = 0
right = len(arr) - 1

while left < right:
    total = arr[left] + arr[right]

    if total == target:
        print(arr[left], arr[right])
        break
    elif total < target:
        left += 1
    else:
        right -= 1

'''Tracing the output
Target = 15

left (idx) | right (idx) | total calculation | condition & action
-----------|-------------|-------------------|---------------------
0 (val: 1) | 5 (val: 15) | 1 + 15 = 16       | 16 > 15 -> right -= 1
0 (val: 1) | 4 (val: 11) | 1 + 11 = 12       | 12 < 15 -> left += 1
1 (val: 2) | 4 (val: 11) | 2 + 11 = 13       | 13 < 15 -> left += 1
2 (val: 4) | 4 (val: 11) | 4 + 11 = 15       | 15 == 15 -> MATCH!

OUTPUT: 4 11'''

