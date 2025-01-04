# #Find the triplets( 3 index of array) in the array with the sum zeros


def findT(arr):
    size =len(arr)
    result = []
    for i in range(0,size-2):

        for j in range(i+1,size-1):

            for k in range(j+1,size):

                if arr[i]+arr[j]+arr[k]==0:
                    result.append([i,j,k])
    return result

arr = [-1,0,1,2,-1,-4]
result = findT(arr)
for triplets in result:
    print(triplets[0],triplets[1],triplets[2])
