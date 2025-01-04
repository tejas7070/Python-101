def Max(arr):
    area = 0
   
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
                       
            area = max(area,min(arr[i],arr[j]) *(j-i))
    return area
arr = [1, 5, 4, 3]

print(Max(arr))
