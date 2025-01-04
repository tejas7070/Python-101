#Given a sorted array of distinct elements arr[]
# of size n that is rotated at some unknown point, the task is to find the minimum element in it. 

def findMin(arr):
    size =len(arr)

    result = arr[0]
    for i in range(1, size):
        result  = min(result, arr[i])
    return result


arr = [99,88,55,66,77]
print("The Minimun element in the rotated Sorted Array-> ",findMin(arr))    