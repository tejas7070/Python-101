#Given a sorted array of distinct elements arr[]
# of size n that is rotated at some unknown point, the task is to find a specific element in it. 

def findMin(arr):
    size =len(arr)
   
    found = False
    for i in range(0, size):
        if element == arr[i]:
            print("Element found", arr[i])
            found = True
            break
    if not found:
        print("Element Not Found")
    return element

       
    


arr = [99,88,55,66,77]

element = int(input("enter the number to searched in the array:"))
findMin(arr)   