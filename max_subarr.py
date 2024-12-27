def maxsub(arr):
    n = len(arr)
    res = arr[0]
    for i in range(1, n):
        cursum = 0
        for j in range(i, n):
            cursum += arr[j]

            res = max(res,cursum)
    return res

arr =[7,-1,2,3,4,6,1]
print(maxsub(arr))  