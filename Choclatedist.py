#Chocolate distribution problem using sliding window


def chocolateDistribution(arr, m):
    n = len(arr)
    arr.sort()
    Mindiff = float("inf")
#For calculating the Minimum difference within a sliding window of size m
    for i in range(n-m+1):

        diff = arr[i+m-1] - arr[i]

        if( diff < Mindiff):
            Mindiff = diff
    return Mindiff

arr = [7, 3, 2, 4, 9, 12, 56] 
m = 5
print(chocolateDistribution(arr, m))       