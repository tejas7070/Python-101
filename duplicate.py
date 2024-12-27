def duplicate(arr):
    n =len(arr)
    for i in range(n):
        for j in range(i+1,n):

            if(arr[i]==arr[j]):
                return True
    return False

arr =[1,2,3,1,2,6]        

print(duplicate(arr))  # Output: True