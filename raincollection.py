def rain(arr):
    res = 0

    for i in range(1, len(arr)):

        left = arr[i]

        for j in range(i):

            left  = max(left,arr[j])

        for k in range (i+1,len(arr)):
            right = arr[i]

            right = max(right,arr[k])

        res += (min(left,right) - arr[i])
    return res

arr = [3,0,2,0,4]
print(rain(arr))  # Output: 7     